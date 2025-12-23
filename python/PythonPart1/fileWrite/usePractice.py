# 대화내용만

# 1. 날짜제거 텍스트 메세지만 저장
# 2. 단어 수 세기
#  오늘은 100  오늘도 200  안녕 300
#  ->무슨 단어를 제일 많이 썼나
 
from datetime import datetime


f = open("C:/PythoneWorkspace/PythonPart1/fileWrite/kakaoChatTock.txt","r",encoding="utf-8")

readLine = f.readlines()
readLine.pop(0)
readLine.pop(1)
readLine.pop(2)
readLine.pop(3)

for line in readLine: 
    if line.startswith("2019"):
        break
    line.strip()
    line = line.split(",")
    cleaned_simple_list = [item.replace('\n', '') for item in line]

    for simple_list in cleaned_simple_list:
        simple_list = simple_list.replace("오후","PM") 
        simple_list = simple_list.replace("오전","AM")
       
        try:
            datetime.strptime(simple_list,"%Y년 %m월 %d일 %p %I:%M")    

        except:
            try:
                print(simple_list.split(":")[1])
            except:
                pass


f.close()