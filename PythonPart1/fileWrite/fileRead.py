# encoding/decoding
#  전 세계적으로 utf-8
# 병렬 저장 관리 = Elasticsearch
# 병렬 전처리  = Hadoop

f = open("C:/PythoneWorkspace/PythonPart1/fileWrite/p05.txt", "r", encoding="utf-8")

# #1) 전체를 다 읽어서 str로
# data = f.read()
# print(data , type(data))


# # 2) 다음 줄 읽어서 str로
# data = f.readline()
# print(data , type(data))
# data = f.readline()
# print(data , type(data))
# data = f.readline()
# print(data , type(data))

# 3) 전체를 다 읽어서, \n기준으로 나눠서 list형태로
# \n을 남겨놨음. 3번이 편해서 많이 사용함. 다만 용량이클때 주의하기
data = f.readlines()
print(data,type(data))


f.close()
