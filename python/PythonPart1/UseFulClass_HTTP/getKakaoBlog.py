# https://developers.kakao.com/
# 4728978749201b35c97c6c303ce804b4


from http.client import HTTPSConnection
import json
from urllib.parse import quote
from lee.LeeStringCleaner import LeeStringCleaner

hc = HTTPSConnection("dapi.kakao.com")

str = input("입력 : ")
str = quote(str)  # 인코딩해서 바꿔주는 라이브러리

hc.request(
    "GET",
    "/v2/search/blog/?query=" + str,
    headers={"Authorization": "KakaoAK 4728978749201b35c97c6c303ce804b4"},
)
resBody = hc.getresponse().read().decode()
resBody = json.loads(resBody)
documents = resBody["documents"]
for doc in documents:
    print(LeeStringCleaner.clean(doc["blogname"]))
    print(LeeStringCleaner.clean(doc["title"]))
    print(LeeStringCleaner.clean(doc["contents"]))
    print("------------")
