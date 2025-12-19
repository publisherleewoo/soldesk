from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import JSONResponse
from product.productDAO import productDAO

app = FastAPI()
pDAO = productDAO()

@app.get("/")
def main():
    return {"hellow": "world"}

h = {
    "Access-Control-Allow-Origin": "http://localhost:5173",
    "Access-Control-Allow-Credentials": "true",
}

@app.post("/product.reg")
async def productReg(photo: UploadFile, name: str = Form(), price: int = Form()):
    result = await pDAO.reg(photo, name, price)
    return JSONResponse(result, headers=h)
