#static member variable
# 중복되는 데이터를 여러번 저장 안하게 -> 메모리 사용량 아껴주는
# 1)Python은 효율적인 프로그램 개발에 무관심
# 2)Python은 static member variable가 있기는 한데, 다른언어처럼 극적인 효과가 없음





# static method
#   일반 method : 객체의 액션(객체가 있어야 사용가능)
# static method : 객체가 없어도 쓸수있는 메소드


##############
# 변수 언제 만드나?  - 데이터 임시저장할때
# 객체 언제 만드나? - 실생활스럽게 데이터 임시저장할때


class Calculator:
    # 멤버변수 없음 - > 저장할거 없음
    @staticmethod
    def printHab(x, y):
        print(x + y)

# 클래스명.메소드   <static메서드
Calculator.printHab(10, 30)


class Calculator2:
    # 멤버변수 없음 - > 저장할거 없음
    def printHab(self,x, y):
        print(x + y)

# 클래스명.메소드   <static메서드
c =Calculator2()
c.printHab(10, 30)
