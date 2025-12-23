from fastapi import FastAPI
from product.productDAO import ProductDAO

app = FastAPI()
pDAO = ProductDAO()

@app.get("/product.reg")
def productReg(name: str, price: int):
    return pDAO.reg(name, price)


@app.get("/product.get")
def productGet(token):
    return pDAO.get(token)
