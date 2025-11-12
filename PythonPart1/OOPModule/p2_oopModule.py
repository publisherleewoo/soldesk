#2
#객체
#제목이 점프 투 파이썬, 가격 30000 책
#정보출력

from p3_exModule import Book

class Mouse:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def printInfo(self):
        print(self.name, self.price)

b = Book("점프투파이썬",30000)
b.show()