# 이름 홍길동, 국어100,영어90,수학80
# 이차원배열보다 아래방식을 선호하자


class Student:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def printInfo(self):
        print(self.name)
        print(self.kor)
        print(self.eng)
        print(self.mat) 


s1 = Student("홍길동", 100, 90, 80)
s1.printInfo()

# Student{
#     name="홍길동"
#     kor=100
#     eng=90
#     mat=80
#     def printInfo(self)
# }


s2 = Student("김길동", 80, 84, 86)
s2.printInfo()

# Student{
#     name="김길동"
#     kor=80
#     eng=84
#     mat=86
#     def printInfo(self)
# }


score = [
         s1,
         s2, 
         Student("최길동", 10, 20, 30),
         Student("이길동", 10, 30, 100),
         Student("박길동", 50, 50, 60)         
         ]


# Student{
#     name="최길동"
#     kor=10
#     eng=20
#     mat=30
#     def printInfo(self)
# }
    
# Student{
#     name="이길동"
#     kor=10
#     eng=20
#     mat=30
#     def printInfo(self)
# }

# Student{
#     name="박길동",
#     kor=50
#     eng=50
#     mat=60
#     def printInfo(self)
# }




# 첫번째 학생의 모든 정보 출력
score[0].printInfo()
#세번째 학생의 국어점수
print("세번째학생의 국어점수",score[2].kor)


def getName(Student):
    print("학생이름 ",Student.name)
    return Student.name

lambdaGetName = (lambda S: S.name)(score[2])
# print(lambdaGetName)

# getName(score[0])
# getName(score[2])

# score.sort(key=lambda S: S.name)

# for s in score:
#     s.printInfo()

def avg(S):
    return (S.kor+S.eng+S.mat)/3
test =(lambda S: S.kor+S.eng+S.mat/3)(score[1])

score.sort(key=lambda S: (S.kor+S.eng+S.mat)/3,reverse=True)

for s in score:
    s.printInfo()
