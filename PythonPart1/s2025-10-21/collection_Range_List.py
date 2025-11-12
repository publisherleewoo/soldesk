## 컬렉션
# list
# set
# dict


# # 범위표현
# a = range(10)  # 0 ~ (10-1)
# print(a)

# b = range(2, 10)  # 2 ~ (10-1)
# print(b)

# c = range(2, 10, 3)  # 2 ~ (10-1), 3칸씩
# print(c)

# # list 1~20
# d = range(1, 21)
# d = list(d)
# print(d)

# # tuple


# x = 10
# y = 20
# (x,y) = (y,x)

# print(x)
# print(y)

# q=100
# w=200
# e=300

# (q,w,e) = (w,e,q)
# print(q)
# print(w)
# print(e)


# def printHab(x,y,z):
#     w= x+y+z
#     print(w)

# def printStrs(o,p):
#     i = o + p

# # override = 자식 함수에서 재정의

# # overloading = 매개변수에 따라 다르게 출력

# def test(a,b,c):
#     print(a,b[0],c[0]) #10,10
#     a=100
#     b[0]=100
#     c=[100,200]
#     print(a,b[0],c[0]) #100,100

# a=10
# b=[10,20]
# c=[10,20]
# print(a,b[0],c[0]) # 10,10
# test(a,b,c)
# print(a,b[0],c[0])# 10,100


# def test(a):
#     print(a)
#     a=100
#     print(a)
# a=10
# print(a)
# test(a)
# print(a)


# 참조타입 : stack에 있는 메모리 주소가 힙메모리의 값을 가르키는것
# def test(b):
#     print(b[0])
#     b[0]=100
#     print(b[0])
# b=[10,20]
# print(b[0])
# test(b)
# print(b[0])


# from time import sleep


# def test(a):
#     print(a%2==0)   #True= 짝수  False =홀수
# test(13)


# def test2(num):
#     return num*2

# d= 10


# result = test2(3)
# print(result)

# def test3(num1,num2):
#     sum = num1+num2
#     sleep(sum)
#     return sum

# print(test3(1,4))

# def tuple(x, y):
#     a = x + y
#     b = x - y
#     c = x * y
#     d = x / y
#     return (a, b, c, d)   #튜플 괄호 생략 가능


# (aa, bb, cc, dd) = tuple(1, 2)

# print(aa)
# print(bb)
# print(cc)
# print(dd)

# lambda함수 : 무명의 1회용 함수
# labmda param변수명,param변수명,...:내용)(값)


# (lambda n: print(n))(123)
# print((lambda a,b,c:(a+b+c)/3)(10,20,55))


# mid = int(input("중간고사 : "))
# final = int(input("기말고사 : "))
# print("-----")
# avg = (mid + final) / 2
# print("평균점수 :%.1f점" % avg)


# if avg >= 80:
#     print("잘했다")
# else:
#     print("나가")
#     if avg >= 70:
#         print("열심히해라")


def getHeight():
    키 = float(input("키:"))
    if 키 > 300:
        return getHeight()
    return 키


def getWeight():
    return  float(input("몸무게:"))


이름 = input("이름 :")
키 = getHeight()
몸무게 = getWeight()



bmi = 몸무게 / ((키 * 키) / 10000)
print("BMI : %.2f" % bmi)

if bmi > 39:
    print("%s씨는 고도" % 이름)
elif 32 < bmi and bmi < 38.9:
    print("%s씨는 중도" % 이름)
elif 30 < bmi and bmi < 36.9:
    print("%s씨는 경도" % 이름)
elif 24 < bmi and bmi < 29.9:
    print("%s씨는 과체중" % 이름)
elif 10 < bmi and bmi < 23.9:
    print("%s씨는 정상" % 이름)
else:
    print("%s씨는 저체중" % 이름)


# 일반인들이 실행하기 용이하게 실행파일까지 만들어줘야
# 1) bat파일
# 2) pyinstaller


# .bat
#   cmd명령어 써놓은 파일
#   실행하면 그 명령어가 실행됨
