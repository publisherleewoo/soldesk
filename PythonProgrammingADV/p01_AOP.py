# 프로그래밍 패러다임
# PP(Procedural Programmin)
#   절차지향 프로그래밍
#   순서대로 잘써서 결과
# OOP(Object Oriented Programing)
#   객체지향프로그래밍
#   실생활을 묘사해서, 유지보수 좋게 하자
# AOP(Aspect Oriented Programming)
#   관점지향프로그래밍
#   OOP를 다른 관점에서 보자
#   +++++메소드들에 있는 공통된 부분들 따로 정리++++++


class Human:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ready(self):
        print("씻고 나갈준비")
        print("엘베타고 1층으로")

    def printInfo(self):
        print(self.name, self.age)

    def goSchool(self):
        self.ready()
        print("버스타고 학교로")

    def goMart(self):
        self.ready()       
        print("걸어서 마트로")

    def goPark(self):
        self.ready()
        print("공원으로")




p1 = Human("홍길동", 30)
p1.printInfo()
p1.goSchool()
p1.goMart()
p1.goPark()
