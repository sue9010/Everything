from bs4 import BeautifulSoup 
import requests

# indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&l=%EC%84%9C%EC%9A%B8&limit=50&radius=25&start=500&vjk=e03c3db92d5c1291")
indeed_result = requests.get("https://indeed.com/jobs?q=python&limit=50")

# print(indeed_result.text)

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all('a')

spans = []
for page in pages:
    spans.append(page.find("span"))
    # print(page.find("span"))

print(spans[:-1])

# print(pages)


