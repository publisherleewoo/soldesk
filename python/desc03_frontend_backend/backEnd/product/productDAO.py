from math import ceil

from fastapi.background import P
from lee.leeDBManager import LeeDBManager


class ProductDAO:
    def __init__(self):
        self.productperPage = 5
        self.setAllProductCount()

    def setAllProductCount(self):
        try:
            con, cur = LeeDBManager.makeConCur()

            sql = "SELECT count(*) FROM dec03_product"
            cur.execute(sql)

            for c in cur:
                self.allProductCount = c[0]

        except Exception as e:
            print(e)
            return None
        finally:
            LeeDBManager.closeConCur(con, cur)

    def get(self, pageNo):
        try:
            con, cur = LeeDBManager.makeConCur()

            pageCount = ceil(self.allProductCount / self.productperPage)

            pageNo = int(pageNo)
            start = (pageNo - 1) * self.productperPage + 1
            end = pageNo * self.productperPage

            sql = (
                "SELECT * FROM (SELECT rownum AS rn,p_no,p_name,p_price,p_stock FROM (SELECT * FROM dec03_product ORDER BY p_no DESC)) WHERE rn>= %d AND rn<=%d"
                % (start, end)
            )

            cur.execute(sql)

            products = []
            for no, name, price, stock, no2 in cur:
                products.append(
                    {"no": no, "name": name, "price": price, "stock": stock, "no2": no2}
                )

            return {"pageCount": pageCount, "products": products}
        except Exception as e:
            print(e)
            return None
        finally:
            LeeDBManager.closeConCur(con, cur)

    def reg(self, n, p, s):
        try:
            con, cur = LeeDBManager.makeConCur()
            sql = "INSERT INTO dec03_product"
            sql += " VALUES (dec03_seq.nextval,"
            sql += "'%s',%d,%d,1)" % (n, p, s)  # 여기에 1이 들어가는게 맞나?
            print(sql)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allProductCount += 1
                return {"result": n + " 등록 성공"}
            return {"result": n + " 등록실패"}

        except Exception as e:
            print(e)
            return {"result": n + " 등록실패"}
        finally:
            LeeDBManager.closeConCur(con, cur)

    def get2(self, pageNo):
        try:
            con, cur = LeeDBManager.makeConCur()
            pageCount = ceil(self.allProductCount / 10)

            pageNo = int(pageNo)
            start = (pageNo - 1) * 10 + 1
            end = pageNo * 10
            sql = (
                "SELECT * FROM (SELECT rownum AS rn,pp_no,pp_name,pp_price,pp_stock FROM (SELECT * FROM dec03_product2 ORDER BY pp_no DESC)) WHERE rn>= %d AND rn<=%d"
                % (start, end)
            )

            cur.execute(sql)

            products = []
            for rn, no, name, price, stock in cur:
                products.append(
                    {"no": no, "name": name, "price": price, "stock": stock}
                )

            return {"pageCount": pageCount, "products": products}
        except Exception as e:
            print(e)
            return None
        finally:
            LeeDBManager.closeConCur(con, cur)
