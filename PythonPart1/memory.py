# snackName="다이제미니"

# print(type(snackName))
# print(snackName)

# print('-----')

# snackPrice=5000
# print(type(snackPrice))
# print(snackPrice)

# print(id(snackName))

# CPU(연산장치)
# RAM(변수형태로 임시저장장치)
# HDD/SSD(파일형태로 영구저장장치)
# GPU(그래픽처리용 CPU+RAM+HDD)

# 변수 (variable)
#   파이썬 문법 사용불가
#   숫자로 시작불가
#   특수문자 사용불가


#파이썬 -번역 ->기계어

# 컴파일 방식 vs 인터프리터 방식
# 소스 전체를 한번에 기계어로 바꿈. 에러있으면 아에 실행불가 
# 프로그래밍언어 ->번역->기계어->실행

# 인터프리터
# 한줄씩 기계어로 바꾸면서 실행
# 인터프리터 방식 프로그래밍 언어

#파이썬 : 프로그래밍 언어
#인터프리터언어
#압축: 공백 제거

#\r carrage return- 커서를 맨앞으로 (이동하기 때문에 맨앞글자 한글자 지움)
#\b backspace(1byte 지우기)       c언어 영어1글자 1byte


#RAM:임시 저장장치
 
#stack -아래쪽에서부터 쌓아 나가는 형태
#heap - OS가 적당하다 싶은 공간을 쌓음
#영화파일,음악파일처럼 거대한 용량의 파일은 stack구조로 차곡차곡 쌓는것이 불가능하기 때문에 heap에 저장 

# snackName = "다이제스트" 의 경우 snackName은 stack에 저장되며, "다이제스트"는 heap에 있다.

# 1byte 8bit
# 컴퓨터가 32bit(4byte)/64bit(8byte)  주소값 저장된 변수(포인터변수)사이즈임.
# ex)컴이 32bit면 램을 4gb이상 못쓰는 이유

# 2의 32승이 4gb대 이기때문에,  주소값 저장된 변수사이즈가 작아서 큰 번지값을 저장 못함.

#python은 변수는 stack에, 모든 데이터를 다 heap에
 

# humidity = 40.345
# print("습도는 %.1f%%입니다" % humidity)

# name = input("폰기종 = ")
# print("모델명은 = %s" %name)
# print("주소값은 = %s" %id(name))
# print("자료형은 = %s" %type(name))


# price = input("폰가격 = ")
# print("입력받은 폰가격 %s"%price)                                                                                                       
# print("주소 %s"%id(price))
# print("자료형 %s"%type(price))


# screenSize = input("화면사이즈 입력")
# screenSize = float(screenSize)
# print("%.2f"%screenSize)

# x = int(input("x:"))
# y = int(input("y:"))

# print("x는 %d, y는 %d" % (x,y))

# a = x+y



# 바퀴둘레 = float(input("바퀴둘레:"))
# 앞기어 = int(input("앞 기어 톱니 수:"))
# 뒷기어=int(input("뒷기어 톱니수:"))
# 발구른횟수=float(input("발 구른 횟수:"))
# 기어비 = 앞기어/뒷기어
# 이동거리=바퀴둘레*발구른횟수*기어비
# print("이동거리 : %.1fcm" % 이동거리)

# price = int(input("구매한 물건 가격"))
# payment =int(input("낸 돈"))


# price = 50000
# payment = 47200
# totalChange = price - payment # 2800

# # 50000원
# 오만원_count = totalChange // 50000 
# totalChange %= 50000 # 남은 돈: 2800

# # 10000원
# 만원_count = totalChange // 10000
# totalChange %= 10000 # 남은 돈: 2800

# # 5000원
# 오천원_count = totalChange // 5000
# totalChange %= 5000 # 남은 돈: 2800

# # 1000원
# 천원_count = totalChange // 1000
# totalChange %= 1000 # 남은 돈: 800

# # 500원
# 오백원_count = totalChange // 500
# totalChange %= 500 # 남은 돈: 300

# # 100원
# 백원_count = totalChange // 100
# totalChange %= 100 # 남은 돈: 0

# # 50원
# 오십원_count = totalChange // 50
# totalChange %= 50 # 남은 돈: 0

# # 10원
# 십원_count = totalChange // 10
# totalChange %= 10 # 남은 돈: 0


# print("오만원 : ", 오만원_count)
# print("만원 : ", 만원_count)
# print("오천원 : ", 오천원_count)
# print("천원 : ", 천원_count)
# print("오백원 : ", 오백원_count)
# print("백원 : ", 백원_count)
# print("오십원 : ", 오십원_count)
# print("십원 : ", 십원_count)



# left_shift 연산자

# 매장속성{
#     와이파이 1<<0 =1
#     24시간  1<<1  =2
#     주차장  1<<2  =4
# }

#매장속성 = 3
#매장속성 =(1 << 0) + (1 << 1)
#매장속성 = 와이파이 + 주차장


# 키 = float(input("키를 입력해주세요"))
# 나이 = int(input("나이를 입력해주세요"))

# a=키>130

# print("키 : %.1fcm" %키)
# print("나이 : %d1" %나이)
# print(a)

# i = True
# j = not i

# print(j)


## &&(and)로 묶을때는 희귀한걸 앞으로

## ||로 묶을때는 일반적인걸 앞으로


# height=100
# age=30

# # XOR 둘중에 하나만 true  둘다 true거나 false면 안됨
# k = (height>=100) ^ (age>=100)
# print(k)

#l은 나이가 20살 미만이든지, 나이가 80살 초과하던지

# age = 20

# l = (age<20) or (80<age)
# m = (10<=age) and (age<=30)
# n = 50<=age

# print(l)
# print(m)
# print(n)



#컬렉션
# 변수중에서 데이터 여러개 담을 수 있는거
# List계열 - list
# Set계열 - set
# Map계열 - dict


# kor =[1,2,3,4,5,6,7,8,9,0] #리스트
# print(kor)
# print(type(kor))
# print(id(kor))
# print(len(kor))
# print(kor[0])
# print(kor.index(2))
 
# print(kor[2:5])  # 인덱스 2번에서 (5-1)번 데이터까지
# print(kor[3:10:2]) # 인덱스 3번부터 (10-1)번 데이터까지 2칸씩
# print(kor[:10:2]) # 처음부터 (10-1)번 데이터까지 2칸씩
# print(kor[3::2])# 인덱스 3번부터 끝까지 2칸씩
# print(kor[3:10:])# 인덱스 3번부터 (10-1)까지
# print(kor[::2])# 시작부터 2칸씩
# print(kor[::-1])# 역순

# s = "그냥 글자를 하나 써봅시다"
# print(s,type(s))
# print(s[1])
# print(s[1:5]) 

# print(kor)


#set : 중복 x
# eng = {12,54,76,12,54,100,33,76}
# print(type(eng))
# print(len(eng))
# print(eng)
# print("-----")



 