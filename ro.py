import requests
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}

def extract_job(html):
  title = html.find("h2", {"itemprop":"title"}).get_text(strip=True)
  company = html.find("h3", {"itemprop":"name"}
                     ).get_text(strip=True).replace('\n', '')
  location = html.find("div", {"class":"location"}).get_text()
  for lc in location:
    if lc == '$': # 위치 정보가 없어서 가격 정보가 출력될 경우
      location = "No office location"
  link = html.find("a", {"class":"preventLink"})['href']
  
  return {
      'title': title,
      'company': company,
      'location': location,
      "link": f"https://remoteok.com/{link}"
  }

def extract_jobs(url):
  jobs = []
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("td", {"class":"company"})

  print("Scrapping ro")
  for result in results:
    check = result.find("h2", {"itemprop":"title"})
    if check is not None:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs(word):
  url = f"https://remoteok.io/remote-dev+{word}-jobs"
  jobs = extract_jobs(url)
  return jobs
