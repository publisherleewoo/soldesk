from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


def htmlFunc(arg1, arg2, arg3, arg4):
    print("내부실행")
    html = ""
    html += "<!DOCTYPE html>"
    html += "<html lang='en'>"
    html += "<head>"
    html += "    <meta charset='UTF-8'>"
    html += "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>"
    html += "    <title>Document</title>"
    html += "</head>"
    html += "<body>"
    html += "    <p style='background-color:%s'>%d %s %s</p>" % (
        arg3,
        arg4,
        arg1,
        round(arg2, 1),
    )
    html += "</body>"
    html += "</html>"
    return HTMLResponse(html)


@app.get("/unit.convert")
def change(a: str, b: str):
    

    a = int(a)
    text=""
    if b == "ci":
        inch = a * 0.393701
        return htmlFunc("센치 인치", inch, "red", a)
    elif b == "mp":
        p = a * 0.3025
        return htmlFunc("제곱미터 평", p, "skyblue", a)
    elif b == "cf":
        f = (a * 1.8) + 32
        return htmlFunc("섭씨 화씨", f, "orange", a)
    elif b == "km":
        mi = a * 0.621
        return htmlFunc("km/h mi/h", mi, "gray", a)
