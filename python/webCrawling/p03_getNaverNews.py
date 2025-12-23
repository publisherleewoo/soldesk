from http.client import  HTTPSConnection
from bs4 import BeautifulSoup
from pymongo import MongoClient


hc = HTTPSConnection("news.naver.com")
hc.request("GET", "/")
resBody = hc.getresponse().read().decode()
hc.close()

con = MongoClient("195.168.9.198") 
db = con.lee

reviewData = BeautifulSoup(
    resBody, "html.parser" 
)  # 받아온거, 내장된 html 파서 이름,인코딩방식

news = reviewData.select(".comp_news_none .cnf_news_list .cnf_news")

 
# print(news)
for n in news:
    print(n.text)
    db.naverNews.insert_one({"txt":n.text})

con.close()