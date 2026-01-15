from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, JSONResponse
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

@app.get("/product.get")
def productGet(page:int):
    result = pDAO.get(page)
    return JSONResponse(result, headers=h)


@app.get("/product.get/{product_id}")
def productGetImg(product_id:str):
    result = f"product/photo/{product_id}"
    return FileResponse(result, headers=h,media_type="image/png")

@app.get("/product.del")
def productDel(name):
    result = pDAO.delete(name) 
    return JSONResponse(result, headers=h)