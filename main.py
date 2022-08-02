from flask import Flask, render_template, request, redirect, send_file
from so import get_jobs as so_get_jobs
from wwr import get_jobs as wwr_get_jobs
from ro import get_jobs as ro_get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
  return render_template("base.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word: 
    word = word.lower() 
    existingJobs = db.get(word)
    if existingJobs: 
      jobs = existingJobs
    else: 
      so_jobs = so_get_jobs(word)
      wwr_jobs = wwr_get_jobs(word)
      ro_jobs = ro_get_jobs(word) 
      jobs = so_jobs + wwr_jobs + ro_jobs
      db[word] = jobs 
  else:
    return redirect("/")
    
  return render_template(
    "report.html", 
    resultNumber = len(jobs), 
    searchingBy=word,
    jobs=jobs 
  )

@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word) 
    if not jobs: 
      raise Exception()
    save_to_file(word, jobs)
    return send_file(f"{word}.csv")
  except:
    return redirect("/")
  
app.run(host="0.0.0.0")