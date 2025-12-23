# Garbage Collection : heap영역 자동정리 시스템
# 그 자동 발동 시점 : 그 번지를 가리키는 변수가 없게 되면 발동
# 어쨋든 Python프로그램은 프로그램 종료시 정리는 다 됨
# 빅데이터를 다뤄야 -> 정리를 빨리 해 줄 필요가 있음



# RAM : 변수형태로 임시 저장공간(컴 끄면 삭제)
# OS가 논리적인 3가지 공간으로 나눠서 사용
# static
# stack : 용량 작은게 저장, 규칙적인 용량이 저장 ->밑에서부터 차곡차곡
# heap : 용량 큰게 저장, 사이즈가 천차만별 - >컴이 적당하다싶은 공간 사용 ->자동정리x, 개발자가 정리해야



class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("학생 없어짐")

    def info(self):
        print(self.name)
        print(self.age)


hong = Person("홍길동", 20)
hong.info()
kim = Person("김길동", 22)
kim.info()

hong=None
kim=None
print("Hong과 Kim ByeBye")

hong2 = Person("홍길동", 20)
hong2.info()

