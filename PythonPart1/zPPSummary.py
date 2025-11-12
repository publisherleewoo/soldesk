# from random import randint

# def getUserAns():
#     userAns = int(input("뭐 :"))
#     if 0 < userAns < 10001:
#         return userAns
#     return getUserAns()

# def pickGameAns():
#     return randint(1,10000)

# def judge(gameAns,userAns):
#     if userAns > gameAns:
#         print("입력하신 숫자가 큽니다 Up")
#     elif userAns < gameAns:
#         print("입력하신 숫자가 작습니다 down")
#     else:
#         print(count, "번만에 맞춤")
#         return False
#     return True

# count=0
# ran =pickGameAns()
# flag = True
# while flag:

#     print(ran)
#     inputNum = getUserAns()
#     count += 1
#     flag = judge(ran,inputNum)


# # from random import randint
# # com,count = randint(1,10000),0
# # while True:
# #     cmt = int(input("뭐 : "))
# #     count = count =+ 1
# #     if cmt > com: print("DOWN!")
# #     elif cmt < com: print("UP")
# #     else: print("정답 %d턴 만에 정답입니다!"% count); break


# from random import randint

# count=0

# def getUserAns():
#     userAns = int(input("뭐 :"))
#     if 0 < userAns < 10001:
#         return userAns
#     return getUserAns()

# def pickGameAns():
#     return randint(1,10000)

# def judge(gameAns,userAns):
#     global count
#     count +=1
#     if userAns > gameAns:
#         print("입력하신 숫자가 큽니다 Up")
#     elif userAns < gameAns:
#         print("입력하신 숫자가 작습니다 down")
#     else:
#         print(count, "번만에 맞춤")
#         return False
#     return True


# ran =pickGameAns()

# while True:
#     print(ran)
#     inputNum = getUserAns()
#     go = judge(ran,inputNum)
#     if not go:
#         break


# from random import randint
# count=0
# def getUserAns():
#     userAns = int(input("뭐 :"))
#     if 0 < userAns < 10001:return userAns
#     return getUserAns()

# def pickGameAns():
#     return randint(1,10000)

# def judge(gameAns,userAns):
#     global count
#     count +=1
#     if userAns > gameAns:print("Up")
#     elif userAns < gameAns:print("down")
#     else:print(count, "번만에 맞춤");return False
#     return True

# ran =pickGameAns()

# while True:
#     print(ran)
#     inputNum = getUserAns()
#     go = judge(ran,inputNum)
#     if not go:
#         break


#######################################################################################################################
##강사님버전##

# from random import randint
# ########################################
# def printRule(handTable):
#     for i, v in enumerate(handTable):
#         if i != 0:
#             print("%d. %s" % (i, v))
#     print("-----")

# def userFire():
#     userHand = int(input("뭐 : "))
#     if 0 < userHand < 4:
#         return userHand
#     return userFire()

# def comFire():
#     return randint(1, 3)

# def printHand(handTable, comHand, userHand):
#     print("컴 : %s" % handTable[comHand])
#     print("나 : %s" % handTable[userHand])

# def judge(comHand, userHand):
#     t = userHand - comHand
#     if t == 0:
#         print("무")
#         return 0
#     elif t == -1 or t == 2:
#         print("패")
#         return 346345423
#     else:
#         print("승")
#         return 1
# ########################################
# handTable = [None, "가위", "바위", "보"]

# printRule(handTable)

# win = 0
# while True:
#     userHand = userFire()
#     comHand = comFire()
#     printHand(handTable, comHand, userHand)
#     result = judge(comHand, userHand)
#     if result == 346345423:
#         print("%d연승" % win)
#         break
#     win += result
#     print("-----")


#     가위    바위    보
# 나  1       2       3
# 컴  1       2       3

# 나 - 컴 = 0  무
# 나 - 컴 = -1 패
# 나 - 컴 = 2  패
# 승


# ##############################################################################################################################
# from random import randint


# def computerRan():
#     return randint(0,2)

# def myInputF(myInput):
#     if(myInput == "가위"):
#         return 0
#     if(myInput == "바위"):
#         return 1
#     if(myInput == "보"):
#         return 2


# computer = computerRan()  ##0= 가위 1=바위 2=보
# count = 0

# # 사용자가 같을때는 비김
# # 사용자가 작을때는 짐
# # 사용자가 클땐 이김, 단 0일경우는 2를 이김   0<1<2<0  나눴을때 나머지로..

# while(True):

#     myInput = input("가위,바위,보=")
#     value = myInputF(myInput)

# !!!!!!!!!!!!!!!!!!3으로 나눴을때 나머지를 체크해서 해야함!!!!!!!!!!!!!!!!!!!!
#     #(value-myInput)%3 ==
#     #(value-myInput)%3 ==
#     #(value-myInput)%3 ==

#     if(value == 0 and computer==0):
#         print("비겼습니다")
#     if(value == 0 and computer==1):
#         print("졌습니다")
#         break
#     if(value == 0 and computer==2):
#         print("이겼습니다")
#         count+=1


#     if(value == 1 and computer==0):
#         print("이겼습니다")
#         count+=1
#     if(value == 0 and computer==0):
#         print("비겼습니다")
#     if(value == 1 and computer==2):
#         print("졌습니다")
#         break


#     if(value == 2 and computer==0):
#         print("졌습니다")
#         break
#     if(value == 2 and computer==1):
#         print("이겼습니다")
#         count+=1
#     if(value == 2 and computer==2):
#         print("비겼습니다")

#     print("연승:",count)


# print((0 - 0) % 3)  # 0  비김
# print((0 - 1) % 3)  # 2  졌음
# print((0 - 2) % 3)  # 1  이김
# print()
# print((1 - 0) % 3)  # 1  이김
# print((1 - 1) % 3)  # 0  비김
# print((1 - 2) % 3)  # 2  졌음
# print()
# print((2 - 0) % 3)  # 2  졌음
# print((2 - 1) % 3)  # 1  이김
# print((2 - 2) % 3)  # 0  비김


# from random import randint


# def computerRan():
#     return randint(0, 2)


# def myInputF(myInput):
#     if myInput == "가위":
#         return 0
#     if myInput == "바위":
#         return 1
#     if myInput == "보":
#         return 2


# computer = computerRan()  ##0= 가위 1=바위 2=보
# count = 0

# # 사용자가 같을때는 비김
# # 사용자가 작을때는 짐
# # 사용자가 클땐 이김, 단 0일경우는 2를 이김   0<1<2<0  나눴을때 나머지로..

# while True:

#     myInput = input("가위,바위,보=")
#     value = myInputF(myInput)

#     total = (value - computer) % 3

#     if total == 0:
#         print("비겼습니다")
#     if total == 1:
#         print("졌습니다")
#         break
#     if total == 2:
#         print("이겼습니다")
#         count += 1

#     print("연승:", count)
