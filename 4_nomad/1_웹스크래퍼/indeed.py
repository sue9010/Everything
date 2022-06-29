from bs4 import BeautifulSoup 
import requests

INDEED_URL = "https://indeed.com/jobs?q=python&limit=50"

def extract_indeed_pages():
    indeed_result = requests.get(INDEED_URL)

    indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

    pagination = indeed_soup.find("div", {"class":"pagination"})

    links = pagination.find_all('a')

    pages = []
    for link in links[0:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]