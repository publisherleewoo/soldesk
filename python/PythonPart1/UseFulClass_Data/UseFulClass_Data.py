# #s =str("뭐 이래요") 이렇게 써야하나
# s = "뭐 이래요" # 약식으로 쓰는것도 허용
# print(s)
# print(type(s))
# print(id(s))
# # Python에는 형변환x ->객체 만드는것 뿐


# s="키\t: %.2fcm" % 180.435343
# print(s)

# # 쓴 모양 그대로 나오게
# s="""ㅋㅋㅋ
# 이렇게 쓸수가
#         있는데요"""
# print(s)

# class dog:
#     def bark(self):
#         print("멍")

# help(dog)
# help(str)

# s = "고기를 한번 잡아봐요"

# # s가 고기는 이라는 말로 시작하는지
# q1 = s.startswith("고기")
# print(q1)
# # s에서 한번->두번으로 바꿔서
# q2 = s.replace("한번", "두번")
# print(q2)
# # s에서 잡 이 몇번째 위치에 있나
# q3 = s.index("잡")
# print(q3)
# # s에서 두번째 글자
# q4 = s[1]
# print(q4)
# # s에 봐 라는 글자가 들어있나
# q5 = s.find("봐")
# print(q5)
# # s 글자수
# q6 = len(s)
# print(q6)



# 데이터 받아오면 str 한덩어리
# -> 분리해서 사용
s = "홍길동,30,수원"
s2 = s.split(",")  #분리해서 list로
print(s2)

s3="       데이터            "
s4 = s3.strip()#앞뒤 공백 제거
print(s4)

s5="!!!!!!!!데이터!!!!!!!!!!"
s6 = s5.strip("!") #앞뒤 그거 제거
print(s6)





# q버전
# 1.9.13
# 1 :major
# 0.13 :minor

# major버전이 0 : 미완성
# major버전이 1 : 완성
# 1.9.13 ->1.9.14 : 거의 체감안되는 변화
# 1.9.13 -> 1.10.0 : 뭔가 다름
# 1.9.13 ->2.0  : 다른 프로그램


# starcraft1
# starcraft2

# python 3.9.13


# help(str)

 