from http.client import HTTPSConnection # <-- 이 부분을 변경해야 합니다.
from urllib.parse import quote

class NaverShoppingDAO:
    def getNSData(self,q):
        print('실행')
        q = quote(q)

        h = {"X-Naver-Client-Id": "NrUNiUV8RrElmIXMx4eO", "X-Naver-Client-Secret": "012diLJrbj"}
        
        huc = HTTPSConnection("openapi.naver.com") 

        huc.request("GET", "/v1/search/shop.xml?query=" + q, headers=h)
        resBody = huc.getresponse().read()
        print(resBody.decode())

        huc.close()
        return resBody.decode()
