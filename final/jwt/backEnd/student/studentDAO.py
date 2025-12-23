from datetime import datetime, timedelta, timezone
from fastapi.responses import JSONResponse
import jwt


#  JWT(Json Web Token)
#   JSON + 암호화 + 시간제한
#   자동갱신x ->직접 갱신해야

#   pip install pyjwt


# 현재시간날짜 : datetime.today()
# 현재시간날짜 : datetime.now()
# 현재시간날짜(표준시간대) : datetime.now(datetime.utc)

# 현재시간날짜(표준시간대)로 부터 10초 지나서 : datetime.now(datetime.utc) + timedelta(seconds=10)


class studentDAO:
    def __init__(self):
        self.jwtkey = "abcd"
        self.jwtAlgorithm = "HS256"

    def reg(self, name, age):
        h = {"Access-Control-Allow-Origin": "*"}
        result = {
            "name": name,
            "age": age,
            "exp": datetime.now(timezone.utc) + timedelta(seconds=10),
        }  # 마음대로 (exp=시간제한)

        jwtResult = jwt.encode(
            result, self.jwtkey, self.jwtAlgorithm
        )  # 암호화해서 str한덩어리로
        print(jwtResult)
        jwtResultResponse = {"myJWT": jwtResult}
        return JSONResponse(jwtResultResponse, headers=h)

    def get(self, encodedJwt):
        try:
            h = {"Access-Control-Allow-Origin": "*"}
            result = jwt.decode(encodedJwt, self.jwtkey, self.jwtAlgorithm)
            result = {
                "result": "복호화한거",
                "name": result["name"],
                "age": result["age"],
            }
        except jwt.ExpiredSignatureError:
            result = {"result": "만들기는 했는데, 시간제한 지난"}
        except jwt.DecodeError:
            result = {"result": "만든적없음"}  # 브라우저 자체를 껐다가 킨 느낌
        return JSONResponse(result, headers=h)

    def update(self, encodedJWT):
        h = {"Access-Control-Allow-Origin": "*"}
        print("업데이트")
        try:
            result = jwt.decode(encodedJWT, self.jwtkey, self.jwtAlgorithm)
            result = {
                "result": "갱신한거",
                "name": result["name"],
                "age": result["age"],
                "exp": datetime.now(timezone.utc) + timedelta(seconds=20),
            }
            result = jwt.encode(result, self.jwtkey, self.jwtAlgorithm)
            result = {"myJWT":result}
            print(result)
        except jwt.ExpiredSignatureError:
            result = {"result": "만들기는 했는데, 시간제한 지난"}
        except jwt.DecodeError:
            result = {"result": "만든적없음"}  # 브라우저 자체를 껐다가 킨 느낌
        return JSONResponse(result, headers=h)
