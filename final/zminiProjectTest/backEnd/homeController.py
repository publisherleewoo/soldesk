from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from board.boardDAO import BoardDAO
from user.userDAO import userDAO

app = FastAPI()
uDAO = userDAO()
bDAO = BoardDAO()

@app.get("/")
def get():
    return {"A": "B"}

headerInfo = {
    "Access-Control-Allow-Origin": "http://localhost:5173",
    "Access-Control-Allow-Credentials": "true",
}

@app.get("/id.check")
def idcheck(u_id):
    result = uDAO.idcheck(u_id)
    print(result)
    return JSONResponse(result, headers=headerInfo)

@app.post("/sign.up")
async def signUp(
    files: UploadFile,
    id=Form(),
    pwd=Form(),
    name=Form(),
    postCode=Form(),
    birthday=Form(),
    addr=Form(),
):
    result = await uDAO.signUp(files, id, pwd, name, postCode, birthday, addr)
    return JSONResponse(result, headers=headerInfo)

@app.post("/login")
def login(id=Form(), pwd=Form()):
    result = uDAO.login(id, pwd)
    print(result)
    return JSONResponse(result, headers=headerInfo)

@app.post("/tokenCheck")
def tokenCheck(memberToken=Form()):
    result = uDAO.tokenCheck(memberToken)
    print(result)
    return JSONResponse(result, headers=headerInfo)

# @app.get('/sign.in.exp.refresh')
# def memberIdCheck(member):
#     print(member)
#     result = uDAO.signInExpRefresh(member)
#     return JSONResponse(result,headers=headerInfo)


@app.get("/get.file/{filename}")
def getFile(filename):
    print(filename)
    result = uDAO.getFile(filename)
    return FileResponse(result, headers=headerInfo)

@app.get("/member.info.get")
def getInfo(member):
    result = uDAO.getInfo(member)
    print(result)
    return JSONResponse(result, headers=headerInfo)


@app.post("/member.info.update")
async def updateInfo(
    files: UploadFile,
    id=Form(),
    pwd=Form(),
    newPwd=Form(),
    name=Form(),
    birthday=Form(),
    postCode=Form(),
    addr=Form(),
):
    result = await uDAO.updateInfo(
        files, id, pwd, newPwd, name, birthday, postCode, addr
    )
    return JSONResponse(result, headers=headerInfo)

@app.get("/member.bye")
def byemember(memberToken):
    result = uDAO.bye(memberToken)
    if result["msg"] == "유저삭제완료":
        bDAO.getBoardCountAll()

    return JSONResponse(result, headers=headerInfo)

@app.get("/board.get")
def getBoard(nowPageNo):
    print(nowPageNo)
    result = bDAO.getBoard(nowPageNo)
    return JSONResponse(result, headers=headerInfo)

@app.get("/board.input.get")
def getInputBoard(str):
    print(str)
    result = bDAO.getInputBoard(str)
    return JSONResponse(result, headers=headerInfo)

@app.post("/board.post")
def postBoard(id=Form(), title=Form(), content=Form()):
    result = bDAO.postBoard(id, title, content)
    return JSONResponse(result, headers=headerInfo)

@app.post("/board.update")
def postBoard(
    boardNo=Form(),
    title=Form(),
    content=Form(),
):
    result = bDAO.updateBoard(boardNo, title, content)
    return JSONResponse(result, headers=headerInfo)

@app.post("/board.delete")
def postBoard(boardNo=Form()):
    result = bDAO.deleteBoard(boardNo)
    return JSONResponse(result, headers=headerInfo)

@app.post("/board.reply.post")
def postReply(boardNo=Form(),id=Form(),reply=Form()):  
    result = bDAO.postReply(boardNo,id,reply)
    return JSONResponse(result, headers=headerInfo)

@app.get("/board.reply.get")
def getReply(postNo):   

    result = bDAO.getReply(postNo)
    print(result)
    return JSONResponse(result, headers=headerInfo)

