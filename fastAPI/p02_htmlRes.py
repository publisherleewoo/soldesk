from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
# uvicorn p01_basic:app --host=0.0.0.0 --port=8888 --reload

@app.get('/html.test')


def test():
    a= 10
    b =20
    c =a+b

    html = "<!DOCTYPE html>"
    html += "<html lang='ko'>"
    html += "<head>"
    html += "<meta charset='UTF-8'>"
    html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
    html += "<title>Document</title>"
    html += "</head>"
    html += "<body>"
    html +=  str(c)
    html += "</body></html>"
    return HTMLResponse(html) #fastAPI는 기본적으로 JSON형태로 뿌려주기때문에 HTMLRESPONSE를 사용해야함
