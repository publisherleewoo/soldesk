# PP(Procedural Programming) : 절차지향프로그래밍
# 절차지향프로그래밍은 함수,조건문 ... 순서대로 잘 써서 프로그램 만들자

# OOP (Object-Oriented Programming) : 객체지향프로그래밍
# 프로그램 소스를 일상언어스럽게 쓰자
# 객체라는걸 써서 리얼월드를 묘사하자

#######
# 개 이름이 후추
# 개 나이 3살
# 그 개가 짖어 : 멍 출력


# class Dog:
#     name = None
#     age = None

#     def __init__(self, param1, param2):
#         self.name = param1
#         self.age = param2

#     def bark(self):
#         print(self.name + "  멍멍")


# dog2 = Dog()

# print(dog2.name)

# dog1 = Dog("후추", 3)
# print(dog1.name)
# print(dog1.age)
# dog1.speak()


# class Cat:
#     name = None
#     age = None
#     def meow(self,cnt):
#         print("냥"*cnt)


# c=Cat()
# c.name="나비"
# c.age=1
# c.weight=3

# Cat.meow(c,5)

# c.meow(5)



# class Phone:
#     model=""
#     num=""
#     price=0
#     def info(self):
#         print("model = ", self.model)
#         print("num = ", self.num)
#         print("price = ", self.price)

# phone = Phone()
# phone.model= "갤s23"
# phone.num= "01031544435"
# phone.price= 300000000

# phone.info()


# class Computer:
#     cpu=""
#     ram=""
#     hdd=""
#     def __init__(self,cpu,ram,hdd):
#         self.cpu=cpu
#         self.ram=ram
#         self.hdd=hdd
#     def info(self):
#         print(
#             "cpu = ",self.cpu,
#             "\nram = ",self.ram,
#             "\nhdd = ",self.hdd
#         )
  
# com1 = Computer("I7","16","HDD")
# com1.info()

class Book:
    def __init__(self,*params):
        print("생성자, 컨스트럭터") #########
        self.title=params[0]
        self.price=params[1]
        print(params[0])
        print(params[1])
    def printInfo(self):
        print(
            self.title,
            self.price)
    def __del__(self):
        print("핸드폰 사라짐")  #########

book1 = Book("점투파이썬",100,200,300)
book1.printInfo()