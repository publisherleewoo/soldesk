# getSubway
# data.seoul.go.kr
#  지하철 -> 서울시 지하철호선별 역별 승하차 인원 정보
#  OpenAPI
# api key = 575a4655496b636839386f58586542
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/5/20151101/
# 2015/01/01 ~ 2024/12/31
# subway.csv
# 2015,01,01,1호선,시청,몇명이타고,몇명이내리고,등록일자
# 2) 2015/11/1 1~5 파싱해서 년,월,일,노선,역,탄,내린 콘솔출력
# 3) 2015/11/1 1~5 파싱해서 년,월,일,노선,역,탄,내린 파일에 쓰기
# 4) 날짜
# 5) 2015/11 한달
#       2015/11/1
#       2015/11/2
#       2015/11/3
#       ...
#       2015/11/30
# 6) 2015 일년
# 7) 2015-2024

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

f = open(
    "C:/PythoneWorkspace/PythonPart1/UseFulClass_HTTP/subway.csv",
    "w",
    encoding="utf-8",
)
hc = HTTPConnection("openapi.seoul.go.kr:8088")
for yy in range(2015, 2025):
    for mm in range(1, 13):
        for dd in range(1, 32):
            when = "%d%02d%02d" % (yy, mm, dd)
            hc.request(
                "GET",
                "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/630/" + when,
            )
            resBody = hc.getresponse().read()

            subwayData = fromstring(resBody)
            rows = subwayData.iter("row")

            for r in rows:
                uy = r.find("USE_YMD").text
                y = uy[0:4]
                m = uy[4:6]
                d = uy[6:8]
                srln = r.find("SBWY_ROUT_LN_NM").text.replace(",", ".")
                ssn = r.find("SBWY_STNS_NM").text.replace(",", ".")
                gont = r.find("GTON_TNOPE").text
                gofft = r.find("GTOFF_TNOPE").text
                data = "%s,%s,%s,%s,%s,%s,%s,\n" % (
                    y,
                    m,
                    d,
                    srln,
                    ssn,
                    gont,
                    gofft
                )
                f.write(data)
            print(when)

hc.close()
f.close()
