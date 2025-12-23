# http://195.168.9.143/index.html

from http.client import HTTPConnection

from bs4 import BeautifulSoup


hc = HTTPConnection("195.168.9.143")
hc.request("GET", "/review.html")
res = hc.getresponse()
resBody = res.read()
txt = resBody.decode()
 

hc.close()

# BeautifulSoup
# Python HTML 파싱 라이브러리
#  pip install bs4

reviewData = BeautifulSoup(
    resBody, "html.parser", from_encoding="utf-8"
)  # 받아온거, 내장된 html 파서 이름,인코딩방식

 

reviews = reviewData.select(".aReview") #css 선택자
for r in reviews:
    tds = r.select("td")
    print(tds[3].text)