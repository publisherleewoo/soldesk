from datetime import datetime
from time import strftime


# deprecated
# 곧 지워질, 삭제될

# 모듈명 : from datetime
# 클래스명 : import datetime
# today()의 정체 : datetime에 있는 static today메서드


# now = datetime.today()  # 현재시간날짜
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now)

# d=datetime(2000,1,1)

# d2 = input("날짜(yyyy/mm/dd) : ")
# d2 = d2.split("/")
# y = int(d2[0])
# m = int(d2[1])
# d = int(d2[2])

# d2 = datetime(y,m,d)
# print(d2)

# 패턴확인
# help(strftime)

d3 = "2000/12/31"
d3 = datetime.strptime(d3,"%Y/%m/%d")
print(d3)

# # 2025.10.30 15:53
# d4 = datetime.today()
# y = d4.year
# m = d4.month
# d = d4.day
# h = d4.hour
# mi = d4.minute

# print("%d.%d.%d %d:%d" % (y,m,d,h,mi))

# #datetime -> str
# d5 = datetime.today()
# d5 = datetime.strftime(d5, "%Y.%m.%d %H:%S")

# print(d5)

d = input("생년월일(YYYY/mm/dd)")
k = datetime.strptime(d, "%Y/%m/%d")
y = k.year

now = datetime.now()
nowY = now.year

yoil =datetime.strftime(k,"%A")

print("요일 : ", yoil)
print("나이 : ", nowY - y+1)


