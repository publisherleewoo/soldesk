# 이름 :
# 가격 : 
# 중량 : 
# -------------> 파일저장
# 이름 :
# 가격 : 
# 중량 : 
# -------------> 파일저장
# 이름 :
# 가격 : 
# 중량 : 
# -------------> 파일저장
# ....
# 이름 : 그만 

f = open("C:/PythoneWorkspace/PythonPart1/fileWrite/snack.csv", "a", encoding="utf-8")

while True:
    ipt= input("이름 : ")
    if(ipt == "그만"):
        break
    ipt2= input("가격 : ")
    ipt3= input("중량 : ")
    print("---------------")
    f.write(ipt+"\n"+ipt2+"\n"+ipt3+"\n")
    f.write(ipt2+"\n")



