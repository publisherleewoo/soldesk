from http.client import HTTPSConnection

from bs4 import BeautifulSoup

 

hc = HTTPSConnection("news.daum.net")
hc.request("GET", "/")
resBody = hc.getresponse().read()
hc.close()



# print(resBody)
 
reviewData = BeautifulSoup(
    resBody, "html.parser", from_encoding="utf-8"
)  # 받아온거, 내장된 html 파서 이름,인코딩방식

 
news = reviewData.select(".item_newsheadline2 .cont_thumb .tit_txt") # css 선택자

for n in news:
    print(n.text)
        