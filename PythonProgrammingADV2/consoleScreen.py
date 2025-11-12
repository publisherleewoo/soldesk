
# name 이라는 변수 : 지역변수?
from guest import Guest

class ConsoleScreen:
    def getGuestInfo():
        name = input("이름 : ")
        height = float(input("키(m) : "))
        weight = float(input("몸무게 : "))
        print(name,height,weight)
        return Guest(name,height,weight)
    def printResult(guest):
        print("BMI : %.2f" % guest.bmi)
        print("%s씨는 %s" % (guest.name, guest.result))
###############################
