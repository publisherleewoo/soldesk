# subway.csv
# 역별로 탄 사람수, 내린사람수 합계내서
# 내린사람수가 더 많은 역명

# 전처리
# csvfile = open("./subway.csv", "r", encoding="utf-8")
# target = {}
# # target = {'서울역':{'input':1000,'output':1000}}

# for row in csvfile.readlines():
#     item = row.split(",")
#     row.replace("\n", "")
#     if item[4] in target:
#         target[item[4]]["input"] += int(item[5])
#         target[item[4]]["output"] += int(item[6])
#     else:
#         target[item[4]] = {"input": int(item[5]),"output": int(item[6]),}
# csvfile.close()

# result = []
# for r in target:
#     if target[r]["input"] < target[r]["output"]:
#         result.append(r)
# print(result)



#분석
f = open("./subway.csv", "r", encoding="utf-8")

rideSum={}
alightSum={}
for line in f.readlines():
    line=line.replace("\n","").split(",") 
    if line[4] in rideSum:
        rideSum[line[4]]+=int(line[5])
        alightSum[line[4]]+=int(line[6])
    else:
        rideSum[line[4]] = int(line[5])
        alightSum[line[4]] = int(line[6])
f.close()

name =[]
ride =[]
alight=[]
for k,v in rideSum.items():
    name.append(k)
    ride.append(v)
    alight.append(alightSum[k])

import numpy as np

name = np.array(name)
ride = np.array(ride)
alight = np.array(alight)
print(name[ride<alight])