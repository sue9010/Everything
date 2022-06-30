from bs4 import BeautifulSoup 
import requests
LIMIT = 50
# URL = f"https://www.jobkorea.co.kr/Search/?stext=python&tabType=recruit&Page_No=2"
URL = f"https://www.jobkorea.co.kr/Search/?stext=python&tabType=recruit"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    try:
        pages = soup.find("div",{"class": "tplPagination newVer wide"}).find_all("a")
    except AttributeError as e:
        pass
    last_page = pages[-2].get_text()
    return int(last_page)

def extract_job(html):
    titles = html.find("a",{"class": "title dev_view"})
    companys = html.find("a",{"class": "name dev_view"})
    location = html.find("span",{"class": "loc long"})
   
    if titles is not None:
        title = titles["title"]
        company = companys["title"]
        location = location.string
        apply_link = "https://www.jobkorea.co.kr/"+titles["href"]
        return {"title": title, "company": company, "location": location,"apply_link": apply_link}
    else:
        pass
    

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&page_No={page+1}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class": "post"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return(jobs)

    

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs