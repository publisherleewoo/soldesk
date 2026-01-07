from pymongo import MongoClient

con = MongoClient("195.168.9.198")
db= con.lee

f = open("C:/PythoneWorkspace/webCrawling/naverNews.txt","a",encoding="utf-8")

news = db.naverNews.find()
for n in news:
    f.write("%s\n" % n["txt"])

f.close()
con.close()