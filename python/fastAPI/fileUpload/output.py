from uuid import uuid4
from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, HTMLResponse

from LeeFileManager import LeeFileManager

# 파일 업로드
# 인코딩 방식이 바뀌어서 오니 pip install python-multipart
# 파일이 업로드 될 폴더 확보(서버)
# 원래 서버에 폴더를 만들어야하는데, 임시적으로 프로젝트 내부에 폴더 만듬

app = FastAPI()


def htmlFunc(title, filename,zipfilename):
    html = ""
    html += "<!DOCTYPE html>"
    html += "<html lang='en'>"
    html += "<head>"
    html += "    <meta charset='UTF-8'>"
    html += "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>"
    html += "    <title>Document</title>"
    html += "</head>"
    html += "<body>"
    html += "<h1>%s</h1>" % (title)
    html += "<h1>%s</h1>" % (filename)
    html += "<img src='/img.get?fName=%s' width='100px'>" % (filename)
    html += "<a href='/zip.get?fName=%s'>다운</a>" %(zipfilename)
    html += "</body>"
    html += "</html>"
    return HTMLResponse(html)


@app.get("/zip.get")
def imgGet(fName: str):
    folder = "./zipFolder/"
    return FileResponse(folder + fName, filename=fName)

@app.get("/img.get")
def imgGet(fName: str):
    folder = "./imggg/"
    return FileResponse(folder + fName, filename=fName)


@app.post("/file.upload")
async def fileUpload(photo: UploadFile, zipp: UploadFile, title: str = Form()):
    photoFolder ="./imggg/"
    filename = await LeeFileManager.upload(photoFolder,photo,"uuid")
    zipFolder ="./zipFolder/"
    zipfilename = await LeeFileManager.upload(zipFolder,photo,"date")

    return htmlFunc(title,filename,zipfilename)


# @app.post("/file.upload")
# async def fileUpload(photo: UploadFile, zipp: UploadFile, title: str = Form()):

#     folder2 = "./zipFolder/"
#     content2 = await zipp.read()  # 파일내용 다 불러오면
#     filename2 = zipp.filename  # 사용자가 업로드한파일명이 back.png라면
#     type2 = filename2[-4:]  # .png
#     filename2 = filename2.replace(type2, "")
#     filename2 = filename2 + "_" + str(uuid4()) + type2  # back_UUID값.png
#     f2 = open(folder2 + filename2, "wb")  # wb : write binary
#     f2.write(content2)
#     f2.close()

#     # 파일 내용을 비동기적으로 모두 읽어 bytes 타입으로 가져옴.
#     # 파일 크기가 매우 크면 메모리 문제가 발생할 수 있음.
#     folder = "./imggg/"
#     content = await photo.read()  # 파일내용 다 불러오면
#     filename = photo.filename  # 사용자가 업로드한파일명이 back.png라면
#     type = filename[-4:]  # .png
#     filename = filename.replace(type, "")
#     # filename = filename + ??? +type
#     # 1 .back20251120121200 날짜,시간으로 가는 전략 (클라이언트가 동시에 이미지를 올려도, 서버측에서 돌기때문에 약간의 시간이 다름. 그래서 결국 유니크한 값이 입력됨)
#     # 2. uuid로 가는 전략
#     # 3. 로그인한 아이디전략

#     filename = filename + "_" + str(uuid4()) + type  # back_UUID값.png

#     f = open(folder + filename, "wb")  # wb : write binary
#     f.write(content)
#     f.close()

#     return htmlFunc(
#         title,
#         filename,
#     )
