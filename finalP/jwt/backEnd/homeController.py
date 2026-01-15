from fastapi import FastAPI
from student.studentDAO import studentDAO


#  JWT(Json Web Token)
#   JSON + 암호화 + 시간제한
#   pip install pyjwt

app =FastAPI()
std =studentDAO()
@app.get('/student.reg')
def get(name:str,age:int):
    print(name,age)
    return std.reg(name,age)

@app.get('/student2.reg')
def getjwt(jwt:str):
    return std.get(jwt)

@app.get('/student.jwt.update')
def updatejwt(jwt:str):
    return std.update(jwt)
