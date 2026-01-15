from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse

from product.productDTO import ProductDTO


app = FastAPI()


@app.get("/")
def main():
    return {"hello": "world"}


@app.post("/pic.post")
async def mainPost(photo: UploadFile, name: str = Form(), price: int = Form()):
    result = await ProductDTO().reg(photo, name, price)
    return JSONResponse(
        result,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
        },
    )
