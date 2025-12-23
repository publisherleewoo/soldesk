## OOD(OBject-Oriented Design)
## 객체지향프로그래밍 스타일 설계
## 1) OOP : 프로그램 소스로 리얼월드 묘사하자
## -> 비만센터에 가서 실제로 비만도 검사하는 씬
## 2) 만들 프로그램에 필요한것만 남기고 객체로 표현할 준비
## 3) 각 객체의 속성(필요한것만)
## 4) 씬 재생 -> 각 객체들의 액션이 보이겠는데
## 5) 만들어가기


# 변수
# 전역변수
# 지역변수
# 파라메터 : 그 행동하는데필요한 재료
# 멤버변수


class Doctor:
    def start(self):
        guest = self.callGuest()
        self.ask(guest)
        self.calculate(guest)

    def callGuest(self):
        return Guest()  # 손님부르고 나면 ->손님이 생김

    def ask(self, guest):
        guest.tell()

    def calculate(self, guest):
        if guest.height > 3:  
            guest.height /= 100
            print(guest.height)
        guest.bmi = guest.weight / (guest.height * guest.height)

        if guest.bmi >= 39:
            guest.result = "고도비만"
        elif guest.bmi >= 32:
            guest.result = "중도비만"
        elif guest.bmi >= 30:
            guest.result = "경도비만"
        elif guest.bmi >= 24:
            guest.result = "과체중"
        elif guest.bmi >= 10:
            guest.result = "정상"
        else:
            guest.result = "저체중"

    def tellResult(self, guest):
        print("BMI : %.2f" % guest.bmi)
        print("%s씨는 %s" % (guest.name, guest.result))


# name 이라는 변수 : 지역변수?
class Guest:
    def tell(self):
        self.name = input("이름 : ")
        self.height = float(input("키(m) : "))
        self.weight = float(input("몸무게 : "))


###############################
d = Doctor()
d.start()
