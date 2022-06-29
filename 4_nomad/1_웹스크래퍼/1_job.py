from bs4 import BeautifulSoup 
import requests

indeed_result = requests.get("https://indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')

pages = []
for link in links[0:-1]:
    pages.append(int(link.string))

max_page = pages[-1]

for n in range(max_page):
    print(n)