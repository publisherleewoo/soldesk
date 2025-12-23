# Python + MongoDB : pymongo.py
from pymongo import MongoClient

# OracleDB
#       table > data
#       SQL로 제어

# MongoDB
#       JS배열 > JS객체
#       JS로 제어
#       -> pymongo -> MongoDB언어를 그대로 사용 가능하게해줌

# 연결
con = MongoClient("195.168.9.108")  # 서버주소[:포트번호]
db = con.nov14  # con.db명
 
# 명령어 + 서버로 전송 + 원격실행
result = db.nov14_student.find().sort({"s_name":1,"s_age":-1})

for s in result:
    print(s["s_name"])
    print(s["s_age"])
    print("--------")
    
# 연결종료
con.close()
