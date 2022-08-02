import requests
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}

def extract_job(html):
  title = html.find("span", {"class":"title"}).get_text()
  company = html.find("span", {"class":"company"}).get_text()
  location = html.find("span", {"class":"region"}).get_text()
  link = html.attrs['href']

  return {
      'title': title,
      'company': company,
      'location': location,
      "link": f"https://weworkremotely.com{link}"
  }

def extract_jobs(url):
  jobs = []
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find("div", {"class":"jobs-container"})
  results = results.find_all("a")

  print("Scrapping wwr")
  for result in results:
    check = result.find("span", {"class":"title"})
    if check is not None:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs(word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  jobs = extract_jobs(url)
  return jobs
