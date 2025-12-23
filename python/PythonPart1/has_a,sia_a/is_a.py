# 다음중 부모클래스,자식클래스간의 상속개념을 가장 잘 나타내는 말은?
# 1. Cat,Dog,  2. Father,Son
# 3. Woman,Man 4. Taxi,Car

# 객체간의 관계로써
# Taxi is a Car  가 성립해야 객체지향프로그래밍이 말하는 상속이다.

# 2번도 son이 나중에 Father가 되니까  Son is a Father라는 논리는 맞는말이다.

# 결론은 모집합과 부분집합의 관계이다.



# #아래는 기본값
# class Dog:(Object):
#     pass




class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def showInfo(self):
        print(self.name, str(self.price) + "원")


# 우리 쇼핑몰의 모든 상품은 상품명/가격
# Product에 있는 멤버들(멤버변수,메소드)이 Pen쪽으로 상속

# Product로 부터 상속받는 Pen
# Product : 상위/부모/super 클래스
# Pen:하위/자식클래스


class Pen(Product):
    pass

    # 정보출력할때 유통기한도 출력하고싶음
    # Product로부터 상속받아온 showInfo는 이름/가격만 출력
    # ovveriding : 상속받아온 메소드 showInfo의 기능 개조


##################

p = Pen("모나미153", 500)
p.showInfo()

# 우유도 상품이라서, 상품명/가격,정보출력
# 우유부터 유통기한 -> 기능확장

# self: 이 클래스
# super: 상위 클래스


class Milk(Product):
    # 상속받은게 아니고 새로만든거 ->생성자 상속이 의미가 있나..
    def __init__(self, name, price, exp):
        super().__init__(name, price)  # Product에 있는 생성자 부른거
        self.exp = exp

    def showInfo(self):
        super().showInfo()  # Product에 있는 showInfo 호출 ->이름, 가격 출력
        print("신발의 사이즈 : ", self.exp)


M = Milk("서울우유1L", 3000, "20251101")
M.showInfo()

# 우유 is a Product
# 품명이 서울우유1L, 가격이 3000원 우유
# 정보출력


class Shose(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def showInfo(self):
        super().showInfo()
        print("신발의 사이즈", self.size)


# 품명이 조던123, 1500000,270사이즈 신발
# 정보출력
M = Milk("조던123", 150000, 270)
M.showInfo()


# 오버라이딩은 상속받은 자식클래스에서 재정의한것(덮어쓰는것)
# 오버로딩은 매개변수에따라 유동적으로 다른 함수 호출


class Computer(Product):
    
    def __init__(self, name, price,cpu,inch,hdd,type):
        super().__init__(name, price)
        self.cpu = cpu
        self.inch = inch
        self.hdd = hdd
        self.type = type
    
    def showInfo(self):
        super().showInfo()
        print(self.cpu,self.inch,self.hdd,self.type)


class Notebook(Computer):
    
  def __init__(self, name, price, cpu, inch, hdd, weight,type):
      super().__init__(name, price, cpu, inch, hdd,type)
      self.weight = weight
  def showInfo(self):
      super().showInfo()
      print("무게",self.weight)



# 품명이 매직스테이션123, 2000000 , i7-1234,32,500 컴퓨터
# 정보출력
print("------")

# 품명이 그램123,2500000,i7-5678,32,1000,3kg,노트북
# 정보출력
com = Computer("매직스테이션123",2000000,"i7-1234",32,500,"컴퓨터")
com.showInfo()

notebook = Notebook("그램123",2500000,"i7-5678",32,1000,"3kg","노트북")
notebook.showInfo()



