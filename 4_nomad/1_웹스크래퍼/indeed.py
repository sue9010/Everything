from bs4 import BeautifulSoup 
import requests
LIMIT = 50
URL = f"https://indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class":"pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[0:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs =[]
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', {"class":"job_seen_beacon"})
    for result in results:
        title = result.find("h2", {"class":"jobTitle"})
        anchor =title.find("a", {"class":"jcs-JobTitle"})
        span = anchor.find("span", {"class":"title"})0
        print(span)
        # anchor = title.find("span")["title"]
        # print(anchor)

    return jobs