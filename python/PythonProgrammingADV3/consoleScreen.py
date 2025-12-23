from datetime import datetime
from company import  company


class ConsoleScreen:
    def getInfo():
        name = input("이름 : ")
        addr = input("주소 : ")
        ceo = input("사장이름 : ")
        emp = input("직원수 : ")
        return company(name, addr, ceo, emp)

    def printResult(result):
        print(result)
    # def getSnackInfo():
    #     name = input("이름 : ")
    #     price = int(input("가격 : "))
    #     weight = int(input("무게 : "))
    #     exp1 = int(input("년 : "))
    #     exp2 = int(input("월 : "))
    #     exp3 = int(input("일 : "))
    #     exp = datetime(exp1, exp2, exp3)
    #     exp = exp.strftime('%Y-%m-%d')
    #     s_c_name=input("회사:")
    #     return Snack(name,price,weight,exp,s_c_name)
