# https://developers.naver.com/ 로그인

# 애플리케이션 등록
#   애플리케이션 이름 : 마음대로
#   사용API:검색
#   비로그인...WEB설정 -> 웹사이트 주소 아무거나 (애플리케이션을 사용할 사이트인데, 나는 임의로 솔데스크학원(https://www.soldesk.org/)등록)

# ClientID : NrUNiUV8RrElmIXMx4eO
# ClientSecret: 012diLJrbj


# Documents - 서비스api - 검색

# request parameter
#   클라이언트가 서버에게 전달하는 정보
#   주소 뒤에

# request header
# 클라이언트가 서버에게 전달하는 정보
# 내부적으로

# 인터넷 주소 체계
#   프로토콜://서버주소(DNS)[:포트번호생략가능]/폴더/폴더/.../파일?변수명=값&변수명=값&변수명=값...


# 실시간 네이벼 뉴스를 AI훈련용 데이터로 확보하는 프로그램
# https://openapi.naver.com/v1/search/news.xml?

# 인터넷 주소에 한글,특수문자x
# ㅋ -> %2A  (URL인코딩)


# 실시간 네이버 스포츠 주소를 훈련용 ai데이터로 확보하는 프로그램


# 1) HTTP통신해서 콘솔출력
# 2) 파싱->제목(title),내용(description) ->콘솔출력
# 3) 날짜, 제목(title),내용(description)->파일에


from datetime import datetime
from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring

from lee.LeeStringCleaner import LeeStringCleaner


q = "야구"
q = quote(q)
# print(q)  #  ㄱㄴ ->%2A URL인코딩

k = {
    "X-Naver-Client-Id": "NrUNiUV8RrElmIXMx4eO",
    "X-Naver-Client-Secret": "012diLJrbj",
}

hc = HTTPSConnection("openapi.naver.com")
hc.request("GET", "/v1/search/news.xml?query=" + q, headers=k)
res = hc.getresponse()
resBody = res.read()
txt = resBody.decode()

data = fromstring(resBody)
itemsss = data.iter("item")
now = datetime.today()
now = datetime.strftime(now, "%Y\t%m\t%d\t%H\t%M")
f = open(
    "C:/PythoneWorkspace/PythonPart1/UseFulClass_HTTP/NaverNews.txt",
    "w",
    encoding="utf-8",
)

for r in itemsss:
    title = LeeStringCleaner.clean(r.find("title").text)
    description = LeeStringCleaner.clean(r.find("description").text)
    data = now + "\t" + title + "\t" + description + "\n"
    f.write(data)

hc.close()
