from uuid import uuid4
from oracledb import connect


class ProductDTO:
    def __init__(self):
        pass

    async def reg(self, photo, name, price):
        try:
            content = await photo.read()
            filename = photo.filename
            type = filename[-4:]
            filename = filename.replace(type, "") + "_" + str(uuid4()) + type

            f = open("./product/photo/" + filename, "wb")
            f.write(content)
            f.close()
        except:
            return "fail"
        finally:
            if filename == "fail":
                return {"result": filename + "등록 실패"}
            try:
                con = connect("leewoo/3214@195.168.9.198:1521/xe")
                cur = con.cursor()
                sql = "INSERT INTO test_dec19 values ('%s',%d,'%s')" % (
                    name,
                    price,
                    filename,
                )
                cur.execute(sql)

                if cur.rowcount == 1:
                    con.commit()
                    return {"result": "등록 성공"}
                return {"result": "등록 실패"}
            except Exception as e:
                return {"result": "등록 실패"}
            finally:
                cur.close()
                con.close()
