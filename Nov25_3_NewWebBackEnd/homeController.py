from fastapi import FastAPI

from snack.snackDAO import SnackDAO

app = FastAPI()
sDAO = SnackDAO()


# ~~~/snackk.regg?n=빼빼로&p=2000
@app.get("/snackk.regg")
def snackReg(n: str, p: int):
    return sDAO.reg(n, p)


# ~~~/snackk.get
@app.get("/snackk.getAll")
def snackGet():
    return sDAO.getAll()


# ~~~/snack.search?page=2&search=칩
# 칩으로 검색해놓은것 페이지 2개만
@app.get("/snack.search")
def snackGet2():
    return sDAO.get()
