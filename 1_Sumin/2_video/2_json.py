import requests
from bs4 import BeautifulSoup
import pandas as pd

# API_Key = "[3. 오픈 API 인증키 파트에서 일반 인증키를 입력해주시면 됩니다.]"
URL = "http://admin:cg600ip100m@192.168.0.34/cgi-bin/httpapi/thermal.cgi?svc=tempAdvInfo&action=gets"

# print(requests.post(URL))
# print(requests.get(URL))
# print(requests.put(URL))

response = requests.get(URL)

response.content
print(response.text)



# API로 데이터 불러오기
# rq = requests.get(URL)
# soup = BeautifulSoup(rq.text, "html.parser")

# cityList = []
# for item in soup.find_all("item"):
#     cityCode = item.find("citycode").text
#     cityName = item.find("cityname").text
#     cityList.append([cityCode, cityName])

# city_df = pd.DataFrame(cityList, columns= ["cityCode", "cityName"])
# city_df.head()


