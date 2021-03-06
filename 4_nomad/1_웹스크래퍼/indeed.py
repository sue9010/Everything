from bs4 import BeautifulSoup 
import requests
LIMIT = 50
URL = f"https://indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
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

def extract_job(html):
    title = html.find("h2", {"class":"jobTitle"}).find("a", {"class":"jcs-JobTitle"}).find("span")
    final_title = title['title']
    company = html.find("span", {"class":"companyName"})
    company_anchor = company.find("a")
    if company.find("a") is not None:
        company =str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    location = html.find("div", {"class":"companyLocation"}).text
    apply_link = html.find("a", {"class":"jcs-JobTitle"})["data-jk"]
    return {'title':final_title, 'company':company, 'location':location, 'link': f"https://www.indeed.com/viewjob?jk={apply_link}"}


def extract_jobs(last_page):
    jobs =[]
    try:
        for page in range(last_page):
            print(f"Scrapping Indeed: Page: {page}")
            result = requests.get(f"{URL}&start={page*LIMIT}")
            soup = BeautifulSoup(result.text, 'html.parser')
            results = soup.find_all('div', {"class":"job_seen_beacon"})
            spans =[]
            for result in results:
                job = extract_job(result)
                jobs.append(job)
    except TypeError as e:
        pass
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
