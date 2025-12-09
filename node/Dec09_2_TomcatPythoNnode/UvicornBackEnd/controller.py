from fastapi import FastAPI
from fastapi.responses import JSONResponse

from product.productDTO import ProductDTO


app = FastAPI()
pDAO = ProductDTO()

@app.get('/')
def get():
    return {"hello":"world"}

@app.get('/product.get')
def get():
    result = pDAO.getProductAll()
    return JSONResponse(result,headers={'Access-Control-Allow-Origin':'*'})

@app.get('/product.reg')
def productReg(name,price):
    result = pDAO.reg(name,price)
    return JSONResponse(result,headers={'Access-Control-Allow-Origin':'*'})
