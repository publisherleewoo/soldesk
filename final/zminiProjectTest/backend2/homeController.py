from fastapi import FastAPI, Form, UploadFile
from user.userDAO import UserDAO

app = FastAPI()
uDAO = UserDAO()


@app.get("/")
def main():
    return {"a": "b"}


@app.post("/sign.up")
async def signUp(
    files: UploadFile = Form(),
    id: str = Form(),
    pwd: str = Form(),
    name: str = Form(),
    birthday: str = Form(),
    postCode: int = Form(),
    addr: str = Form(),
):
    await uDAO.reg(id, pwd, name, birthday, postCode, addr, files)

    pass
