from os import remove
from oracledb import connect
from lee.LeeFileManager import LeeFileManager


class productDAO:
    def __init__(self):
        self.photoDir = "./product/photo/"

    async def reg(self, photo, name, price):

        filename = await LeeFileManager.upload(
            self.photoDir, photo, "uuid", 10 * 1024 * 1024
        )  ## 10메가
        if filename == "fail":
            return {"result": filename + "등록 실패"}

        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = "INSERT INTO dec19_product values ('%s',%d,'%s')" % (
                name,
                price,
                filename,
            )
            
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return {"result": filename + "등록 성공"}
            return {"result": filename + "등록 실패"}
        except Exception as e:
            remove(self.photoDir + filename)  # 파일 지우기
            return {"result": filename + "등록 실패"}
        finally:
            cur.close()
            con.close()
