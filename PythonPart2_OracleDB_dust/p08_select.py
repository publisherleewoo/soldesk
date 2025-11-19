# 서울 미세먼지 11/03 두번째 파싱해서 db에
# 1) 서울시 실시간 미세먼지 파싱해서 db서버에 저장하는 프로그램
# 2) db서버에 저장되어있을 그 미세먼지 데이터를 csv로 만드는 프로그램
# 3) openweathermap 파싱해서 db서버에 저장
# 4) db서버 저장되어 있을 그 날씨 데이터를 csv로 만드는 프로그램

# 2025/11/03 10:52에 실행하면
# 2025/11/03 10:52서울 미세먼지 저장

# 실행하면 실시간 서울 미세먼지 csv에출력
# 2025,11,03,10,52,도심권,중구,10,5,좋음
 
from xml.etree.ElementTree import fromstring
from oracledb import connect

f = open("C:/PythoneWorkspace/PythonPart2_OracleDB/seoulDust.csv", "a", encoding="utf-8")

con = connect("leewoo/3214@195.168.9.53:1521/xe")

sql = "select * from seoul_dust"

cur = con.cursor()
cur.execute(sql)
for date,MSRRGN_NM,MSRSTN_NM,PM10,PM25,IDEX_NM in cur:
    string_kr = date.strftime("%Y,%m,%d,%H,%M")
    f.write(string_kr+","+MSRRGN_NM+","+MSRSTN_NM+","+str(PM10)+","+str(PM25)+","+IDEX_NM+","+'\n')
 
cur.close()
con.close()

f.close()