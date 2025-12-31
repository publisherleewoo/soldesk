from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from user.userDAO import userDAO


app = FastAPI()
uDAO = userDAO()

@app.get("/")
def get():
    return {"A": "B"}

@app.get('/id.check')
def idcheck(u_id):
   result =  uDAO.idcheck(u_id)
   print(result)
   return JSONResponse(result,headers={'Access-Control-Allow-Origin':'http://localhost:5173','Access-Control-Allow-Credentials':'true'})

@app.post("/sign.up")
async def signUp(files: UploadFile,id=Form(),pwd=Form(),name=Form(),postCode=Form(),birthday=Form(),addr=Form()):
    result = await uDAO.signUp(files,id,pwd,name,postCode,birthday,addr)
    return JSONResponse(result,headers={'Access-Control-Allow-Origin':'http://localhost:5173','Access-Control-Allow-Credentials':'true'})

@app.post("/login")
def login(id=Form(), pwd=Form()):
    result = uDAO.login(id, pwd)
    print(result)
    return JSONResponse(result,headers={'Access-Control-Allow-Origin':'http://localhost:5173','Access-Control-Allow-Credentials':'true'})

@app.get('/sign.in.exp.refresh')
def memberIdCheck(member):
    print(member)
    result = uDAO.signInExpRefresh(member)
    return JSONResponse(result,headers={'Access-Control-Allow-Origin':'http://localhost:5173','Access-Control-Allow-Credentials':'true'})

@app.get('/get.file/{filename}')
def getFile(filename):
    result = uDAO.getFile(filename)
    return FileResponse(result,headers={'Access-Control-Allow-Origin':'http://localhost:5173','Access-Control-Allow-Credentials':'true'})
#  id ,password, name, 사진,나이,이름


@app.get('/member.info.get')
def getFile(member):
    
    pass
    # result = uDAO.getFile(filename)
    # return FileResponse(result,headers={'Access-Control-Allow-Origin':'http://localhost:5173','Access-Control-Allow-Credentials':'true'})
#  id ,password, name, 사진,나이,이름
