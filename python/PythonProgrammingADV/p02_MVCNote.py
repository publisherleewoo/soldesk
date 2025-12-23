# 실무 프로젝트
# 고객
# PM
# MVC 패턴 : 파일 나눠서 작업, 한파일은 한명이 끝까지
#   파일이 하나 있으면, M/V/C중에 하나의 역할만
#   Model: 비지니스 로직(실제 계산)
#   View : 실제로 눈에 보이는, 입력받고 결과 출력
#   Controller: 흐름 제어(View가 필요하면 View,Model 필요하면 Model)

x = int(input())
y = int(input())
z = x + y
print(z)
