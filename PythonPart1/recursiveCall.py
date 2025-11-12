# 함수명(1) = 1

# 함수명(2) = 함수명(1) + 2 = 3
# 함수명(3) = 함수명(2) + 3 = 6
# 함수명(4) = 함수명(3) + 4 = 10

# 함수명(n) = 함수명(n-1) + n 



# def 함수명(num):
#     if num != 1:
#         return 함수명(num - 1) + num
#     else:
#         return 1


# print(함수명(10))







# 1! = 1 = 1
# 2! = 1 x 2 = 2
# 3! = 1 x 2 x 3 = 6

# factorial(1) = 1
# factorial(2) = factorial(1) x 2 = 1 x 2
# factorial(3) = factorial(2) x 3 = 1 x 2 x 3


# def factorial(num):
#     if num != 1:
#         return factorial(num-1) * num
#     else:
#         return 1

# def factorial(num):
#     if num != 1:
#         return factorial(num-1) * num
#     return 1

# print(factorial(5))





# 숫자를 하나 넣으면 그 위치의 피보나치수열 값 구하는 함수
# 1 2 3 4 5 6 7 - 위치
# 1 1 2 3 5 8 13  -값

# fibo(1) = 1
# fibo(2) = 1
# fibo(3) = fibo(1)+fibo(2)
# fibo(4) = fibo(2)+fibo(3)
# fibo(5) = fibo(3)+fibo(4)
# fibo(6) = fibo(4)+fibo(5) 


# def fibo(num):
#    if(num==1 or num==2):
#       return 1
#    return fibo(num-2)+fibo(num-1)
 
    
# print(fibo(50))



# 함수를 사용하면 속도는 느려지기때문에 위에 같은 로직은 반복문이 더 효율적임.



# #짝수를 입력받을때까지 함수 호출
# def getEven():
#    no = int(input("짝수 : "))    
#    if no%2== 0:  #짝수면
#       return no #받은것을 결과로
#    else: #홀수면
#       return getEven() #다시 함수실행
# no = getEven()
# print("입력한숫자는 %d"%no )



# flag = True
# while(flag):
#     no = int(input("짝수 :"))
#     if( no%2 == 0):
#         flag =False
#         break
#     else:
#         flag=True
#         continue