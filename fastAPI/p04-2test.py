from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


def htmlFunc(arg1, arg2,arg3,arg4):
    print("내부실행")
    return HTMLResponse(
        f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p style="background-color:{arg3}">{arg4}{arg1}{round(arg2,1)}</p>
</body>
</html>"""
    )


@app.get("/change")
def change(a: str, b: str):
    a = int(a)
    if b == "ci":
        inch = a * 0.393701

        return htmlFunc("센치인치", inch,"red",a)
    elif b == "mp":
        p = a * 0.3025
        return htmlFunc("미터제곱평", p,"skyblue",a)
    elif b == "cf":
        f = (a * 1.8) + 32
        return htmlFunc("섭씨화씨", f,"orange",a)
    elif b == "km":
        mi = a * 0.621
        return htmlFunc("km/h->mi/h", mi,"gray",a)
