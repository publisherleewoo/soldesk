# 서울 열린 데이터광장 https://data.seoul.go.kr/
# 주소/포트/...을 공개했기 때문에 해킹위험히 있음
# 그래서 로그인->신청을해야 줌
# api key값 = 575a4655496b636839386f58586542

#미세먼지 ->공공데이터 더보기 
# 서울시 권역별 실시간 대기환경 현황
# http://openAPI.seoul.go.kr:8088/(인증키)/xml/RealtimeCityAir/1/5/
# http://openAPI.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/5/

#1) HTTP 통신걸어서 통신 출력


from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# 'http://' 부분을 제거
hc = HTTPConnection("openapi.seoul.go.kr:8088") 

# 요청 경로(URI)는 그대로 유지
hc.request("GET","/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/") 
res = hc.getresponse()
resBody = res.read()
txt = resBody.decode() 

# print(txt)

hc.close()

# XML (eXtended Markup Language)
# 데이터를 HTLM모양으로 표현해놓은
# DOM (Document Object Model) 객체

seoulDustData = fromstring(resBody) #xml파싱시작
rowsss = seoulDustData.iter('row') # <row></row>들 
for r in rowsss:
   print(r.find("MSRRGN_NM").text)
   print(r.find("MSRSTE_NM").text)
   print(r.find("PM10").text)
   print(r.find("PM25").text)
   print(r.find("IDEX_NM").text)
   