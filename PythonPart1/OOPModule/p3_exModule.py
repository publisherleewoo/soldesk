# 3
# class
from p2_oopModule import Mouse

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def show(self):
        print("책이름 = ", self.title, "책가격 =", self.price)

m = Mouse("로지텍",10000)
m.printInfo()