from bs4 import BeautifulSoup 
import requests

indeed_result = requests.get("https://indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all('a')

spans = []
for page in pages:
    spans.append(page.find("span"))

print(spans[:-1])
