from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/xmll.test")
def xmlTest():
    xml = "<?xml version='1.0' encoding='UTF-8'?>"
    xml += "<snacks>"
    xml += "     <snack>"
    xml += "         <s_name>초코파이</s_name>"
    xml += "         <s_price>5000</s_price>"
    xml += "     </snack>"
    xml += "     <snack>"
    xml += "         <s_name>마이쮸</s_name>"
    xml += "         <s_price>2000</s_price>"
    xml += "     </snack>"
    xml += "</snacks>"
    h={"Access-Control-Allow-Origin":"*"}
    return Response(xml, media_type="application/xml", headers=h)


@app.get("/jsonn.test")
def xmlTest():
    json = [
        {"n_name": "초코파이", "s_price": 5000},
        {"n_name": "마이쮸", "s_price": 2000},
    ]
    # XML/JSON을 외부에서도 사용 가능하게 하려면
    # Access-Control-Allow-Origin 응답 헤더를 세팅
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(json, headers=h)
