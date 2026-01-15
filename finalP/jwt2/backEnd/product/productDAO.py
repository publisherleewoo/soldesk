from datetime import datetime, timedelta, timezone
from fastapi.responses import JSONResponse
import jwt


class ProductDAO:
    def __init__(self):
        self.key = "1234"
        self.algorithm = "HS256"

    def reg(self, name, price):
        h = {"Access-Control-Allow-Origin": "*"}
        product = {
            "name": name,
            "price": price,
            "exp": datetime.now(timezone.utc) + timedelta(seconds=5),
        }
        token = jwt.encode(product, self.key, self.algorithm)

        return JSONResponse(
            {"token": token},
            headers=h,
        )

    def get(self, token):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            product= jwt.decode(token,self.key,self.algorithm)
        except:
            product ={"name":"없","price":"음"}
        return JSONResponse(product,headers=h)