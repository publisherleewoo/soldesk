# has a 관계
#Human has a Dog
#Dog Has a Huamn

class 벼룩틀:
    def __init__(self,name,size):
        self.name=name
        self.size=size

    def show(self):
        print(self.name, self.size)


########
# 이름이 벼룩, 크기가 1mm인 벌레

벼룩인스턴스 = 벼룩틀("벼룩이","1mm")  #벼룩틀로 생성된 벼룩인스턴스
벼룩인스턴스.show()


class Dog:
    def __init__(self, name, breed,벼룩파라미터):
        self.name = name
        self.breed = breed
        self.벼룩멤버변수 = 벼룩파라미터
    def infoPrint(self):
        print(self.name, self.breed)
        print("has a 관계, 강아지에게 붙어있는 벼룩", self.벼룩멤버변수.name)


# 이름이 후추, 종이 말티즈 강아지
dog1 = Dog("후추", "말티즈",벼룩인스턴스)
 
class Person:
    def __init__(self, name, age, pet):
        self.name = name
        self.age = age
        self.pet = pet

    def infoPrint(self):
        print(self.name, self.age, self.pet.name)
        self.pet.infoPrint()

# 이름이 홍길동, 30살, 후추,말티즈 인스턴스를 가지고 있음.  이부분이 has a 관계
hong = Person("홍길동", 30, dog1)
hong.infoPrint()


# class Test:
#     pass

# print(type(0))
# print(type(""))
# print(type([]))
# print(type(lambda x:x))
# print(type(Test))
# print(type(Test()))
# print(type(None))


