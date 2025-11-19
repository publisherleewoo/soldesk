 # pip install fastapi
# pip install uvicorn[standard]

# 파일경로로 가서 uvicorn 파일명(확장자말고):app --host=0.0.0.0 --port=???? --reload
# uvicorn p01_basic:app --host=0.0.0.0 --port=8888 --reload


from fastapi import FastAPI

app = FastAPI()

@app.get('/te.st')
def test():
    snack ={'name':'초코파이','price':5000} #fastAPI는 기본적으로 JSON형태로 뿌려줌
    return snack