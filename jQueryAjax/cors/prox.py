from fastapi import FastAPI, Response

from dao import NaverShoppingDAO


app = FastAPI()
nsDAO = NaverShoppingDAO()


# http://127.0.0.1:8000/naver.shopping.get?q=
@app.get("/naver.shopping.get")
def proxyGet(q: str):
    result = nsDAO.getNSData(q)
   
    h = {"Access-Control-Allow-Origin": "*"}
    return Response(result, media_type="application/xml", headers=h)
