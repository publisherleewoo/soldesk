from fastapi import FastAPI
from fastapi.responses import JSONResponse

from menu.menuDTO import MenuDTO


app = FastAPI()
mDto = MenuDTO()


@app.get("/menu.reg")
def reg(name, price, desc):
    print(name,price,desc)
    result = mDto.regMenu(name, price, desc)
    return JSONResponse(result, headers={"Access-Control-Allow-Origin": "*"})

@app.get("/menu.get")
def get(pageNo):
    print('pageNo',pageNo)
    result = mDto.getMenu(pageNo)
    return JSONResponse(result, headers={"Access-Control-Allow-Origin": "*"})

@app.get("/menu.delete")
def get(name):
    print('name',name)
    result = mDto.deleteMenu(name)
    return JSONResponse(result, headers={"Access-Control-Allow-Origin": "*"})

 