from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Optional

app = FastAPI()


def test(id, pw, gender, addr, hobby, comment):

    html = "<!DOCTYPE html>"
    html += "<html lang='ko'>"
    html += "<head>"
    html += "<meta charset='UTF-8'>"
    html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
    html += "<title>Document</title>"
    html += "</head>"
    html += "<body>"
    html += "아디 :" + (id) + "<br/>"
    html += "비번 : " + (pw) + "<br/>"
    html += "성별 : " + (gender) + "<br/>"
    html += "주소 : " + (addr) + "<br/>"
    if hobby != None:  # checkBox일때
        html += "<h3>취미</h3>"
        for h in hobby:
            html += (h) + "<br/>"
    comment = comment.replace("\r\n", "<br>")
    html += "소개 : " + (comment) + "<br/>"
    html += "</body></html>"
    return HTMLResponse(
        html
    )  # fastAPI는 기본적으로 JSON형태로 뿌려주기때문에 HTMLRESPONSE를 사용해야함


# checkbox : 변수하나에 값 여러개 -> 주소에 표현불가 . POST방식이여야
#   변수명:Optional[list[자료형]]자료형=Form()
@app.post("/member.sign.up")
def join(
    id: str = Form(),
    pw: str = Form(),
    gender: str = Form(),
    addr: str = Form(),
    hobby: Optional[list[str]] = Form(None),  # checkbox일때
    comment: str = Form(),
):
    print(comment)
    return test(id, pw, gender, addr, hobby, comment)
