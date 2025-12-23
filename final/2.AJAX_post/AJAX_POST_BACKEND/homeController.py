from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from calculator.calculator import Calculator

app = FastAPI()
c = Calculator()


@app.get("/get")
def get():
    return {"hello": "world"}


@app.get("/calculator.do")
def calculator(x: int, y: int):
    result = c.calculator(x, y)
    return JSONResponse(result, headers={"Access-Control-Allow-Origin": "*"})


#   cross origin resource sharing으로써 보안상 막는 브라우저에서 다른 ip 접속을 허용할지 유무를 정해주는것


@app.post("/calculator.do2")
def calculator(x: int = Form(), y: int = Form()):
    result = c.calculator(x, y)
    return JSONResponse(
        result, headers={"Access-Control-Allow-Origin": "*"}
    )  # 접근한 모든 서버에게 주겠다


## 파일업로드 설정
@app.post("/calculator.do3")
def calculator(x: int = Form(), y: int = Form()):
    result = c.calculator(x, y)
    return JSONResponse(
        result,
        headers={
            "Access-Control-Allow-Origin": "http://localhost:5173",
            "Access-Control-Allow-Credentials": "true",
        },
    )  # http://localhost:5174만 Cross-Domain AJAX가 가능하게
