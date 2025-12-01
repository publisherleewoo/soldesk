from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/product.reg")
def testapi(p_name: str, p_price: str):
    print("#######################접속###############")
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>"""
    html += p_name + "<br>"
    html += p_price + "<br>"
    html += "</body></html>"

    return HTMLResponse(html)
