from calendar import c
from uuid import uuid4
from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import JSONResponse

from photo.photoManager import PhotoManager

app = FastAPI()
pm = PhotoManager()


@app.get("/")
def get():
    return {"a": "b"}


h = {
    "Access-Control-Allow-Origin": "http://localhost:5173",
    "Access-Control-Allow-Credentials": "true",
}

@app.post("/photo.upload")
async def post(file: UploadFile, title: str = Form()):
    result = await pm.upload(file, title)
    return JSONResponse(result, headers=h)

@app.get('/photo.get')
def photoGet(filename):
    return pm.get(filename)