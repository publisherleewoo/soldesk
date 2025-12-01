from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

# uvicorn p02_htmlRes:app --host=0.0.0.0 --port=8888 --reload
app = FastAPI()


def htmlBasic(arg):
    html = "<!DOCTYPE html>"
    html += "<html lang='ko'>"
    html += "<head>"
    html += "<meta charset='UTF-8'>"
    html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
    html += "<title>Document</title>"
    html += "</head>"
    html += "<body>"
    html += str(arg)
    html += "</body></html>"
    return HTMLResponse(html)  # HTMLRESPONSE추가


@app.get("/xy.calculate2")
def xyCalculate(start: str, end: str):  # reqParam변수명:자료형,....
    x = start
    y = end
    print(x, y)
    print(type(x), type(y), "문자열이기 때문에 형변환")
    x = int(x)
    y = int(y)
    dans = ""
    for dan in range(x, y + 1):

        dans += "<h1>%d단</h1>" % (dan)
        for i in range(1, 10):
            dans += "<p> %d x %d = %d</p>" % (dan, i, dan * i)

    return htmlBasic(dans)


# post방식으로 reqParam받는건
# pip install python-multipart
@app.post("/gugudanPost.show")
def gugudan(start: str = Form(), end: str = Form()):  # reqParam변수명:자료형=Form(),...
    x = start
    y = end
    print(x, y)
    print(type(x), type(y), "문자열이기 때문에 형변환")
    x = int(x)
    y = int(y)
    dans = ""
    for dan in range(x, y + 1):

        dans += "<h1>%d단</h1>" % (dan)
        for i in range(1, 10):
            dans += "<p> %d x %d = %d</p>" % (dan, i, dan * i)

    return htmlBasic(dans)
