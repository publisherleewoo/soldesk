from fastapi import FastAPI
from fastapi.background import P
from fastapi.responses import JSONResponse
from product.productDAO import ProductDAO
from seller.sellerDAO import SellerDAO

app = FastAPI()
sDAO = SellerDAO()
pDAO = ProductDAO()

@app.get("/")
def ab():
    return {"hello": "world"}

@app.get("/seller.get")
def selletGet(page):
    result = sDAO.get(page)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)

@app.get("/seller.get.detail")
def selletGet(no):
    result = sDAO.getDetail(no)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)

@app.get("/seller.update")
def selletDelete(no,name,addr):
    result = sDAO.getUpdate(no,name,addr)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)


@app.get("/seller.delete")
def selletDelete(no):
    result = sDAO.getDelete(no)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)



@app.get("/product.get")
def productGet(page):
    result = pDAO.get(page)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result,headers=h)

@app.get("/product2.get")
def productGet2(page):
    result = pDAO.get2(page)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result,headers=h)


@app.get("/seller.reg")
def sellerReg(s_name, s_birthday, s_addr):
    result = sDAO.reg(s_name, s_birthday, s_addr)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)

@app.get('/product.reg')
def ab(p_name,p_price,p_stock):
    result = pDAO.reg(p_name,int(p_price),int(p_stock))
    h={"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)



