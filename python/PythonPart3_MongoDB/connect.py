# Python + MongoDB : pymongo.py
from pymongo import MongoClient

#연결
con = MongoClient("195.168.9.108")  # 서버주소[:포트번호]
db = con.nov14  # con.db명

print(con)
print(db)

con.close()