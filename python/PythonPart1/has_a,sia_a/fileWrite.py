# 맥,윈도우,리눅스 등등 베이스가 달라서 맞춰줘야됨
# WORA(Write Once, Run Anywhere)
# 원래 시스템별로 프로그램을 다 다르게 만들어야 하는데 시스템별로 프로그램 다르게 안만들어도 되는

# 요즘 나오는 언어들은 대부분 WORA가 기본.  ex)자바부터

# 파일열기
# 윈도우
# f= open("C:/kim")
# 리눅스
# f= open("/kim")

# encoding : 사람의 데이터를 전기신호로
# decoding : 전기신호를 사람의 데이터로
# 음악 ->인코딩 ->0101011
# 영상 ->디코딩 ->1011111


# 데이터 -> 임시저장 : 변수형태로 RAM에 저장
#  -> 영구저장 : 파일형태로 SDD/HDD에 저장

msg = input("뭐 : ")
for _ in range(3):
    print(msg)

# 파일 열기 (폴더는 안만들어줌, 파일은 만들어줌)
f = open("C:/PythoneWorkspace/PythonPart1/fileWrite", "a", encoding="utf-8")

f.write(msg + "\n")
f.close()
