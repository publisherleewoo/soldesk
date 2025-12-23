class ConsoleScreen:
    def __init__(self):
        print("1.등록")
        print("2.모두 가져오기")
        print("3.특정 책제목 입력해서 가져오기")
        print("4.수정")
        print("5.삭제")
        print("--------")
        print("10.종료")

    def inputFunc(self):
        return input("뭐 : ")
    
    def printInfo(self,info):
        print(info)