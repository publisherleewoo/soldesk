# 어벤져스
#   본명
#   나이
#   정보출력기능 -> 본명/나이 출력
#   공격하기기능 ->공격하기 출력


class Avengers:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print(self.name, "", self.age)

    def attack(self):
        print("공격하기")

class Human:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def eat(self):
        print("냠")

    def printInfo(self):
        print(self.name, self.address)

#다중상속일경우 이름이 같으면?
# Avengers에 printInfo
# Human에 printInfo
# ->먼저 상속받은것   (아래는 Avengers)

class IronMan(Avengers,Human): 
    def __init__(self, name, age, comName):
        super().__init__(name, age)
        self.comName = comName
        
    def printInfo(self):
        super().printInfo()
        print(self.comName)

    def attack(self):
        print("빔 발사")


# Product           아래로 갈수록 구체화, 위로갈수록 추상화
# Computer
# NoteBook


tony = IronMan("토니", 40, "자비스")
tony.attack()
tony.eat()
tony.printInfo()
