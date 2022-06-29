from typing import final
from bs4 import BeautifulSoup 
import requests
LIMIT = 50
URL = f"https://indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    try:
        pagination = soup.find("div", {"class":"pagination"})
        links = pagination.find_all('a')
        pages = []
        for link in links[0:-1]:
            pages.append(int(link.string))
        max_page = pages[-1]
        return max_page
    except AttributeError as e:
        pass

def extract_indeed_jobs(last_page):
    jobs =[]
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', {"class":"job_seen_beacon"})
    spans =[]
    for result in results:
        title = result.find("h2", {"class":"jobTitle"}).find("a", {"class":"jcs-JobTitle"}).find("span")
        final_title = title['title']
        print(final_title)
    return jobs