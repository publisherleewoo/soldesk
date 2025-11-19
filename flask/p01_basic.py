# Web Server
#   HTML/CSS를 올려놓으면 클라이언트가 요청했을때 HTML/CSS를 응답해주는 서버

# WAS(Web Application Server)
#   Web Server + 프로그램 실행되는

# Flask : Python WAS 라이브러리
# 시작 - cmd
#   pip install flask

# HTTP통신
#   클라이언트가 서버에 요청하면
#   서버는 그 요청에 대해 응답

from flask import Flask

app = Flask(__name__)




 

@app.get("/te.st")  # /te.st라는 주소로 클라이언트로부터 GET방식 요청받으면
def test():
    return "abcd"  # abcd라고 응답


# 응답

if __name__ == "__main__":
    # 접속허용해주는 주소.  0.0.0.0일경우 아무나 접속가능
    # 두번째 인자는 포트번호
    # 세번째 인자는 디버그모드(로그출력,자동재시작)여부
    app.run("0.0.0.0", 9999, True)
