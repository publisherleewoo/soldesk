# analysisSubway
# 요일별 이용객수(탄사람 + 내린사람) 평균
# -> 무슨요일 이용객수 가장 많

# 1) 그 파일 부분만 읽어서 콘솔출력
# 2) 요일, 탄, 내린 콘솔출력
# 3) 요일별로 평균???


from datetime import datetime


f = open(
    "C:/PythoneWorkspace/PythonPart1/UseFulClass_HTTP/subway.csv", "r", encoding="utf-8"
)

 
class abc:
    def test():
        pass


 
subwaySum = {"Sun": 0, "Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0}
subwayCnt = {"Sun": 0, "Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0}
for line in f.readlines():
    line = line.replace("\n", "").split(",")
    when = "%s,%s,%s" % (line[0], line[1], line[2])
    when = datetime.strptime(when, "%Y,%m,%d")   # datetime 객체를 뱉는거
    yoil = datetime.strftime(when, "%a") # datetime객체를 문자열로 뱉는거
    sum = int(line[5]) + int(line[6])
    subwaySum[yoil] += sum
    subwayCnt[yoil] += 1
f.close()

# for k, v in subwaySum.items():
#     print(k, (v / subwayCnt[k]))

# print(subwaySum)
# print(subwayCnt)


# f = open(
#     "C:/PythoneWorkspace/PythonPart1/UseFulClass_HTTP/subway.csv", "r", encoding="utf-8"
# )

# line = f.readlines()
# avg= {
#     "0":0,
#     "1":0,
#     "2":0,
#     "3":0,
#     "4":0,
#     "5":0,
#     "6":0
# }
# arr =[0,0,0,0,0,0,0]
# for text in line:
#         y = text.split(",")[0] #년
#         m = text.split(",")[1] #월
#         d = text.split(",")[2] #일
#         gont = int(text.split(",")[5]) #탄
#         gofft = int(text.split(",")[6]) #내린
#         print("%s %s %s"%(y,m,d))
#         k = datetime.strptime("%s %s %s"%(y,m,d), "%Y %m %d")
#         weekday = k.weekday()

#         if weekday == 0: #월
#             avg["0"] += gont+gofft
#             arr[0] +=1
#         if weekday == 1: #화
#             avg["1"] += gont+gofft
#             arr[1] +=1
#         if weekday == 2: #수
#             avg["2"] += gont+gofft
#             arr[2] +=1
#         if weekday == 3: #목
#             avg["3"] += gont+gofft
#             arr[3] +=1
#         if weekday == 4: #금
#             avg["4"] += gont+gofft
#             arr[4] +=1
#         if weekday == 5: #토
#             avg["5"] += gont+gofft
#             arr[5] +=1
#         if weekday == 6: #일
#             avg["6"] += gont+gofft
#             arr[6] +=1

# print("월",avg["0"]/arr[0])
# print("화",avg["1"]/arr[1])
# print("수",avg["2"]/arr[2])
# print("목",avg["3"]/arr[3])
# print("금",avg["4"]/arr[4])
# print("토",avg["5"]/arr[5])
# print("일",avg["6"]/arr[6])
