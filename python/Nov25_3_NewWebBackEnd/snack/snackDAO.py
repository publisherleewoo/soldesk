from lee.leeDB import LeeDB


class SnackDAO:
    # def __init__(self):
    #     self.sellerPerPage=3

    # def get(self, pageNo, searchTxt):
    #     try:
    #         con, cur = LeeDB.dbstart()
    #         searchTxt = "%" + searchTxt + "%"
    #         pageNo = int(pageNo)
            
    #         start = (pageNo - 1) * self.sellerPerPage + 1
    #         end = pageNo * self.sellerPerPage

    #         sql = "SELECT * from(SELECT rownum AS rn,s_no,s_name,s_addr,s_birthday FROM (SELECT * FROM nov11_seller where S_NAME LIKE '%s' or s_addr LIKE '%s'" % (
    #             searchTxt,
    #             searchTxt,
    #         ) + "ORDER BY s_name)) WHERE rn>=%d AND rn<=%d" % (
    #             start,
    #             end,
    #         )
    #         print(sql)
    #         cur.execute(sql)

    #         sellers = []
    #         for _, no, name, addr, birthday in cur:
    #             print(cur)
    #             s = Seller(no, name, addr, birthday)
    #             sellers.append(s)

    #         return sellers

    #     except Exception as e:
    #         print(e)
    #         return None
    #     finally:
    #         LeeDB.dbclose(con, cur)

    def getAll(self):
        try:
            con, cur = LeeDB.dbstart()
            sql = "select * from nov52_snack order by s_name"
            cur.execute(sql)

            snacks = []
            for name, price in cur:
                snacks.append({"s_name": name, "s_price": price})
            return snacks
        except Exception as e:
            print(e)
            return None
        finally:
            LeeDB.dbclose(con, cur)

    def reg(self, nn, pp):
        try:
            con, cur = LeeDB.dbstart()
            sql = "INSERT INTO nov52_snack VALUES ('%s',%d)" % (nn, pp)
            print(sql)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return {"result": nn + " 등록성공"}
            return {"result": nn + " 등록실패"}
        except Exception as e:
            return {"result": nn + " 등록실패"}
        finally:
            LeeDB.dbclose(con, cur)
