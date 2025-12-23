from flask import Flask, request


app = Flask(__name__)


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
    return html


# request parameter : 클라이언트가 was로 보내는 정보

# 인터넷 주소 체계
# 프로토콜:://서버IP주소:포트/지정한주소?변수명=값&변수명=값&...

# HTTP통신 요청
#   GET방식
#       주소 직접 쳐서 접속, <a>->일반적
#   POST방식
#       form/프로그램을 통해서만 가능 -> 특수
#       reqParam이 내부적으로 전달 - >보안성 높음


# http://195.168.9.153.8888/xy.calculate2?xxx=10&yyy=20
@app.get("/xy.calculate2")
def xyCalculate():
    # request.args.get('reqParam변수명')
    x = request.args.get("start")
    y = request.args.get("end")
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


@app.post("/gugudanPost.show")
def gugudan():
    x = int(request.form["start"])
    y = int(request.form["end"])

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


if __name__ == "__main__":
    app.run("0.0.0.0", 8888, True)
