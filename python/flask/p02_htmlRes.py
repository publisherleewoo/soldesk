from flask import Flask


app = Flask(__name__)


@app.get("/html.test")
def htmlTest():
    html = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>안녕하세요</h1>
</body>
</html>"""
    return html




@app.get("/xy.calculate")
def xyCalculate():
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
    return html



@app.get("/gugudan.show")
def gs():

    html = "<!DOCTYPE html>"
    html += "<html lang='ko'>"
    html += "<head>"
    html += "<meta charset='UTF-8'>"
    html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
    html += "<title>Document</title>"
    html += "</head>"
    html += "<body>"

    for dan in range(2, 10):
        html += "<h1>%d단</h1>" % (dan)
        for i in range(1, 10):
            html += "<p>%d x %d = %d</p>" % (dan, i, dan * i)
    html += "</body></html>"
    return html





# def htmlBasic(arg):
#     html = "<!DOCTYPE html>"
#     html += "<html lang='ko'>"
#     html += "<head>"
#     html += "<meta charset='UTF-8'>"
#     html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
#     html += "<title>Document</title>"
#     html += "</head>"
#     html += "<body>"
#     html +=  str(arg)
#     html += "</body></html>"
#     return html

# @app.get('/testFunc')
# def testFunc():

#     return htmlBasic("<p>문자열테스트</p>")






if __name__ == "__main__":
    app.run("0.0.0.0", 8888, True)
