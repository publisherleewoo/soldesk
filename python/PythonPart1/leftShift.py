# 1<<2
#   1 -> 1
#  100->4


####  2진법의 숫자를 역순으로 제거하면 좋은기능 ####


# 와이파이  1<<0  1
# 24시간 1<<1  2
# 흡연실 1<<2  4
# 주차장 1<<3  8






# value = int(input("매장 특성 : "))

# if value >= (1 << 3):
#     print("주차장")
#     value -= 1 << 3

# if value >= (1 << 2):
#     print("흡연실")
#     value -= 1 << 2

# if value >= (1 << 1):
#     print("24시간")
#     value -= 1 << 1

# if value >= (1 << 0):
#     print("와이파이")
#     value -= 1 << 0






# value = int(input("매장 특성 : "))

# dict={
#     3:"주차장",
#     2:"흡연실",
#     1:"24시간",
#     0:"와이파이",
# }


# for (key,v) in dict.items() :
#     if value >= (1 << key):
#         print(v)
#         value -= 1 << key












# value = int(input("매장 특성 : "))
# option=["와이파이","24시간","흡연실","주차장"]
# for i in range(len(option)-1, -1,-1):
#     if value >= (1<<i):
#         print(option[i])
#         value -= (1<<i)













# value = int(input("매장 특성 : "))

# if(value==1<<0): #1
#     print("#와이파이")
# if(value==1<<1): #2
#     print("#24시간")
# if(value==(1<<0)+(1<<2)+(1<<3)): #13
#     print("#와이파이")
#     print("#흡연실")
#     print("#주차장")


# 1
# 와이파이

# 2
# 24시간

# 13
# 와이파이
# 흡연실
# 주차장


