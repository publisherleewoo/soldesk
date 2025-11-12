# 로도 번호 자동
# 1 ~ 45사이의 중복없게 랜덤한 숫자 6개


# 첫번째 숫자 : 그냥 뽑기
# 두번째 숫자 : 일단 뽑고, 첫번째 숫자랑 같은지, 다르면 그냥 같으면 다시 뽑고 또 체크
# 세번째 숫자: 일단 뽑고, 첫/두번째 숫자랑 같은가 다르면 그냥 같으면 다시 뽑고, 또 체크



# from random import randint

# def pick(i, lotto):
#     l = randint(1, 6)    #랜덤한수
#     # 첫번째
#     # 두번째 : 첫번째
#     # 세번째 : 1,2

#     # i = 0  x
#     # i = 1  0
#     # i = 2  0,1
#     for j in range(i):  
#         if l == lotto[j]: 
#             return pick(i,lotto)
#     return l

# lotto = []
# for i in range(6):
#     l = pick(i, lotto)
#     lotto.append(l)

# print(lotto)



# from random import randint

# list = list(range(1,46)) 
# result = [] 
 
# for _ in range(6):
#     i = randint(0, len(list) - 1)
#     pick = list.pop(i) 
#     result.append(pick)




#list 를 넣으면 오름차순을 정렬해주는 함수
# 첫번째값과 두번째 값 비교 => 첫번째 값이 작으면 앞으로
# 두번째값과 세번째 값 비교 => 두번째 값이 작으면 앞으로
# 세번째값과 네번째 값 비교 => 세번째 값이 작으면 앞으로
# 네번째값과 다섯번째값 비교 => 세번째값이 작으면 앞으로



# 처음에는 이렇게짜고
# def bubbleSort(l):
#    for _ in range(len(l)-1): 
#     for n in range(len(l)-1):  # 0~3
#         if l[n] >l[n+1]:
#             l[n],l[n+1] =l[n+1],l[n]
            
# l = [765,213,21,1786,2]
# bubbleSort(l)
# print(l)

# #0턴일때 돌지 않게 만드는 방법
# def bubbleSort(l):
#    for turn in range(len(l)-1):  #0~3
#     for n in range(len(l)-1-turn):  #0턴 :01 12 23 34, 1턴 01 12 23
#         if l[n] >l[n+1]:
#             l[n],l[n+1] =l[n+1],l[n]
            
# l = [765,213,21,1786,2]
# bubbleSort(l)
# print(l)





## step1) 제일 작은 수 찾기
# def selecttionSort(l): 
#     min =l[0]
#     for i in range(1,len(l)):
#        if min > l[i]:
#           min = l[i]
#     print(min)
         
# li =[765,213,21,1786,2]
# selecttionSort(li)



# # step2) 자리바꾸는 작업해야되는데, 제일작은값이 있던 값, 위치
# def selecttionSort(l): 
#     min = l[0]
#     minIndex = 0
#     for i in range(1,len(l)):
#        if min > l[i]:
#           min = l[i]
#           minIndex = i
#     print(min,minIndex)
         
# li =[765,213,21,1786,2]
# selecttionSort(li)



# # step3)전체 바꾸기
# def selecttionSort(l): 
#     for turn in range(0,len(l)-1):  # 0~3턴까지
#         min = l[turn]  #일단은 turn번이 최소값이라고 가정
#         minIndex = turn # 최소값이 turn번에 있다고 가정
#         for i in range(turn+1,len(l)):  #1,2,3,4
#             if min > l[i]:   # 최소값 값보다 다음뻔째 값이 작으면
#                 min = l[i]   # 그것이 최소값
#                 minIndex = i  # 그 최소값의 인덱스는 i번째 있는거
#         l[turn],l[minIndex] = l[minIndex], l[turn]   # turn번이랑 최소값 있는 위치 자리바꾸기

#         print(min,minIndex)
#         print(l)
         
# li =[765,213,21,1786,2,500]
# selecttionSort(li)










#turn = 0 
#min =l[0] =765
#minIndex = 0
#i = 1
# if 765 >211:
#   min=211
#   minIndex = 1