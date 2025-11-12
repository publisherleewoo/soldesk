# 2025/11/03 10:52에 실행하면
# 2025/11/03 10:52서울 미세먼지 저장

# 실행하면 실시간 서울 미세먼지 csv에출력
# 2025,11,03,10,52,도심권,중구,10,5,좋음

from datetime import datetime
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")
res = hc.getresponse()
resBody = res.read()
txt = resBody.decode()


seoulDustData = fromstring(resBody)
rowsss = seoulDustData.iter("row")
hc.close()

now = datetime.today()
now = datetime.strftime(now, "%Y,%m,%d,%H,%M")
print(now)

f = open(
    "C:/PythoneWorkspace/PythonPart1/UseFulClass_HTTP/SeoulDust.csv",
    "a",
    encoding="utf-8",
)
for r in rowsss:
    MSRDT = r.find("MSRDT").text
    MSRRGN_NM = r.find("MSRRGN_NM").text
    MSRSTE_NM = r.find("MSRSTE_NM").text
    PM10 = r.find("PM10").text
    PM25 = r.find("PM25").text
    IDEX_NM = r.find("IDEX_NM").text
    data = "%s,%s,%s,%s,%s,%s\n" % (
        now,
        MSRDT,
        MSRRGN_NM + "," + MSRSTE_NM,
        PM10,
        PM25,
        IDEX_NM,
    )
    f.write(data)
    print(data)



f.close()

