# 이 파일 윈도우 스케줄러에 등록해서 bat확장자로, 오전에한번 오후에 한번 실행하기.
# 9시30분한번, 2시10분한번 하면 될듯.

# 서울 미세먼지 11/03 두번째 파싱해서 db에
# 1) 서울시 실시간 미세먼지 파싱해서 db서버에 저장하는 프로그램
# 2) db서버에 저장되어있을 그 미세먼지 데이터를 csv로 만드는 프로그램
# 3) openweathermap 파싱해서 db서버에 저장
# 4) db서버 저장되어 있을 그 날씨 데이터를 csv로 만드는 프로그램

# 2025/11/03 10:52에 실행하면
# 2025/11/03 10:52서울 미세먼지 저장

# 실행하면 실시간 서울 미세먼지 csv에출력
# 2025,11,03,10,52,도심권,중구,10,5,좋음




 
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
from oracledb import connect


hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")
res = hc.getresponse()
resBody = res.read()
txt = resBody.decode()
hc.close()
#################
con = connect("leewoo/3214@195.168.9.198:1521/xe")

seoulDustData = fromstring(resBody)
rowsss = seoulDustData.iter("row")
for r in rowsss:
    MSRRGN_NM = r.find("SAREA_NM").text
    MSRSTN_NM = r.find("MSRSTN_NM").text
    PM10 = r.find("PM").text
    PM25 = r.find("FPM").text
    IDEX_NM = r.find("CAI_GRD").text
    sql = "INSERT INTO seoul_dust values(sysdate,'%s','%s',%s,%s,'%s')" % (
        MSRRGN_NM,
        MSRSTN_NM,
        PM10,
        PM25,
        IDEX_NM,
    )

    print(sql)

    cur = con.cursor()  # DB작업 총괄매니저(1회용)
    cur.execute(sql)
    con.commit()
    cur.close()

con.close()
