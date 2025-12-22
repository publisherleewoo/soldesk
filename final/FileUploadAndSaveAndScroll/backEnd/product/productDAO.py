from math import ceil
from os import remove
from oracledb import connect
from lee.LeeFileManager import LeeFileManager


class productDAO:
    def __init__(self):
        self.photoDir = "./product/photo/"
        self.productPerPage = 5
        self.setAllProductCount()

    def setAllProductCount(self):
        con = con = connect("leewoo/3214@195.168.9.198:1521/xe")
        cur = con.cursor()
        sql = "select count(*) from dec19_product"
        cur.execute(sql)
        for a in cur:
            self.allProductcount = a[0]

    def delete(self, name):
        try:
            con = con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            filename = self.getPhotoFileName(name)

            sql = "delete dec19_product where a_name = '%s'" % (name)
            cur.execute(sql)
            # 이미지도 동시삭제 해야됨
            if cur.rowcount == 1:
                self.allProductcount -= 1
                con.commit()
                remove(self.photoDir + filename)
                return {"result": "db삭제성공"}
            return {"result": "db삭제실패"}
        except Exception as e:
            print(e)
            return {"result": "db삭제에러"}
        finally:
            cur.close()
            con.close()

    def getPhotoFileName(self, name):
        try:
            con = con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = "SELECT p_photo from dec19_product where a_name = '%s'" % (name)
            cur.execute(sql)
            for name in cur:
                print(name[0])
                return name[0]
        except:
            return "없음"
        finally:
            cur.close()
            con.close()

    def get(self, page):

        try:
            con = con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()

            pageCount = ceil(self.allProductcount / self.productPerPage)

            start = (page - 1) * self.productPerPage + 1
            end = page * self.productPerPage

            sql = (
                "SELECT * FROM  (SELECT rownum AS rn, a_name,a_price,p_photo FROM (select * from dec19_product ORDER BY a_name)) WHERE %d<=rn and rn<=%d"
                % (start, end)
            )
            cur.execute(sql)
            products = []
            for _, name, price, photo in cur:

                products.append({"name": name, "price": price, "photo": photo})
            print(pageCount)
            print(products)
            return {"pageCount": pageCount, "products": products}
        except Exception as e:
            print(e)
        finally:
            cur.close()
            con.close()

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
                self.allProductcount += 1
                return {"result": filename + "등록 성공"}
            return {"result": filename + "누가 이미 지운 이미지입니다"}
        except Exception as e:
            remove(self.photoDir + filename)  # 파일 지우기
            return {"result": filename + "등록 실패"}
        finally:
            cur.close()
            con.close()
