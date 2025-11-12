# # 반복문


# list = [45, 234, 11, 100, 50]
# for item in list:
#     print(item)

# print()


# for i in range(0, 5):
#     print(i)

# print()


# for i in range(0, 11, 2):
#     print(i)

# print()


# l = ["ㅋ", "ㅎ", "ㅠ", "ㅡ"]
# for i in range(len(l)):
#     print(l[i])

# print()


# # 튜플 반환
# for i in enumerate(l):
#     print(i)

# print()


# # 튜플 반환이기때문에 아래처럼 가능
# for index, value in enumerate(l):
#     print(index, value)

# dict = {"색깔": "검정", "가격": 500}

# print()


# # 딕셔너리 키,벨류값
# for key, value in dict.items():
#     print(key, value)

# print()


# for i in range(1,10,2):
#     print(i)

# print()

# for i in range(9,0,-2):
#     print(i)

# print()


# for i in range(1, 10):
#     print("2 x %d = %d" % (i, 2 * i))

# print()


# for i in range(1, 10):
#     for j in range(2,10):
#             print("%d x %d = %d "%(j,i,i*j), end="\t")
#     print()


# from time import sleep


# for i in range(5):
#       for j in range(5):
#             print("ㅋ",end="")
#       print()
#       sleep(0.5)


# #ㅋ
# #ㅋㅋ
# #ㅋㅋㅋ
# #ㅋㅋㅋㅋ
# #ㅋㅋㅋㅋㅋ

# for k in range(1,6):
#     print(k*"ㅋ")
# print()

# #ㅋㅋㅋㅋㅋ
# #ㅋㅋㅋㅋ
# #ㅋㅋㅋ
# #ㅋㅋ
# #ㅋ

# for k in range(5,0,-1):
#     print(k*"ㅋ")
# print()

# # ㅋ
# #  ㅋ
# #   ㅋ
# #    ㅋ
# #     ㅋ

# for j in range(0,5):
#     print(j*" ","ㅋ")
# print()


# for i in range(0,5):
#     for j in range(0,i+1):
#          print("ㅋ",end="")

#     print()
# print()


# #i = 0
# #j = range(0,1) // 0

# #i = 1
# #j = range(0,2) // 0,1

# #i = 2
# #j = range(0,3) // 0,1,2

# #i = 3
# #j = range(0,4) // 0,1,2,3,4

# for i in range(0,5):
#     for j in range(5-i,0,-1):
#          print("ㅋ",end="")

#     print()


# ㅋ  #     0 , 0
# pㅋ  #    1 , 1
# ppㅋ  #   2 , 2
# pppㅋ  #  3 , 3
# ppppㅋ  # 4 , 3
# pppppㅋ


# for i in range(0,5):
#     for j in range(0,i):
#         print(" ",end="")
#     print("ㅋ")


# ㅋ   i = 0  j = 0
# ㅎㅎㅎ  i = 1 j = 2
# ㅋㅋㅋㅋㅋ i = 2 j = 4
# ㅎㅎㅎㅎㅎㅎㅎ i = 3  j = 6
# ㅋㅋㅋㅋㅋㅋㅋㅋㅋ i = 4 j = 8

# for i in range(0,5):
#     for j in (0,2*i):
#         print(j)


# for i in range(1, 6):
#     if i % 2 == 1:
#         print("ㅋ" * (i + i - 1))
#     else:
#         print("ㅎ" * (i + i - 1))
# print()


# for i in range(5):
#     for j in range(2*i+1):
#         if i%2 == 1:
#             print("ㅎ",end="")
#         else:
#             print("ㅋ",end="")
#     print()


# s="ㅋ"
# for i in range(5):
#      if (i%2 == 1):
#         s = "ㅎ"
#      else:
#         s = "ㅋ"
#      for j in range(2*i+1):
#         print(s,end="")
#      print()


# 1부터 20까지 더하기
# count = 0
# for a in range(1,21):
#     count +=a
# print(count)


# count = 0
# for a in range(1,21):
#     count +=a
#     if(count>100):
#         print(a,"를 더한 순간 100을 넘습니다.")
#         print("count값은.", count)
#         break


# from random import randint


# b = randint(1, 5)  # 1~5사이의 랜덤한 정수

# print(b)
# print("-----")

# 1~10사이의 랜덤한 정수
# 10번


# for a in range(0,10):
#     print(randint(0,10))


# for a in range(0,10):
#     c = randint(0,10)

#     print(c)

#     if c == 4:
#         print(c,"4가 나왔습니다")
#         break


# while (True):
#     c = randint(0, 10)
#     print(c)
#     if c == 4:
#         break


# flag = True
# while (flag):
#     c = randint(0, 10)
#     print(c)
#     if c == 4:
#         flag = False
 
# while(True):
#     e = int(input("숫자 : "))
#     print(e)
#     if(e == 5):
#         break

# i = 1
# while(i<=101):
#     print(i)
#     i+=3


# while(True):
#     chat = input("뭐 : ")
#     print(chat)
#     if(chat == "나가"):
#         break




# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if(k==1):
#                 break #가까운 for k in range(3):가 깨짐
#             print(i,j,k)



# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if(k==1):
#                 break; #가까운 for k in range(3):가 깨짐
#             print(i,j,k)




#### 다 깨는방법


# def 함수명():
#     for i in range(3):
#         for j in range(3):
#             for k in range(3):
#                 if(k==1):
#                     return; #가까운 for k in range(3):가 깨짐
#                 print(i,j,k)
# 함수명()



# flag = False
# for i in range(3):  # 0,1,2
#     if(flag == True):
#         break
#     for j in range(3):  # 0,1,2
#          if(flag == True):
#             break
#          for k in range(3): #0,1,2
#             if(k==1):
#                 flag =True; #가까운 for k in range(3):가 깨짐
#                 break
#             print(i,j,k)



