from datetime import datetime
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()
app.mount(
    "/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static"
)


def resulthtml(u_name, u_height, u_weight, bmi, result, filename):

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
 
 <div>
    <h1>비만도검사</h1>
    <img src="/img.get?fName={filename}" width="100px"><br/>
    <label for="u_name">이름:</label><input value={u_name} disabled><br />
    <label for="u_height">키:</label><input value={u_height} disabled><br />
    <label for="u_weight">몸무게:</label><input value={u_weight} disabled><br />
    <label>bmi</label><input value={bmi} disabled><br />
    <label>결과</label><input value={result} disabled><br />
</div>
 
</body>
</html>"""
    return html


@app.get("/")
def bmiCheck():
    return {"msg": "안녕하세요"}


@app.get("/img.get")
def imgGet(fName: str):
    return FileResponse("./img/" + fName)


@app.post("/bmi")
async def bmiCheck(
    u_photo: UploadFile,
    u_name: str = Form(),
    u_height: float = Form(),
    u_weight: float = Form(),
):
    content = await u_photo.read()


    filename = u_photo.filename
    extname = filename[-4:]
    filename = filename.replace(extname, "")
    now = datetime.today()
    now = datetime.strftime(now, "%Y%m%d%H%M%S")
    filename = filename + "_" + now + extname

    f = open("./img/" + filename, "wb")
    f.write(content)
    f.close()

    bmi = u_weight / (u_height * u_height / 10000)

    result = ""
    if bmi < 18.5:
        result = "저체중"
    elif 18.5 < bmi < 23.0:
        result = "정상"
    elif 23 < bmi < 25:
        result = "과체중"
    else:
        result = "비만"

    html = resulthtml(u_name, u_height, u_weight, bmi, result, filename)
    return HTMLResponse(html)
