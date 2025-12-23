from calendar import c
from datetime import datetime
from math import ceil
from lee.leeDBManager import LeeDBManager


class SellerDAO:
    def __init__(self):
        self.sellerPerPage = 5
        self.setAllSellerCount()

    def getDetail(self,no):
        no = int(no)
        try:
            con, cur = LeeDBManager.makeConCur()

            sql ="SELECT * FROM dec03_seller where s_no = %d" % no

            cur.execute(sql)          
            for no, name, bd, addr in cur:
                bd = datetime.strftime(bd,'%Y/%m/%d')
                return {"no":no,"name":name,"bd":bd,"addr":addr}
    
        except Exception as e:
            print(e)
            return None
        finally:
            LeeDBManager.closeConCur(con, cur)

    def getDelete(self,no):
        no = int(no)
   
        try:
            con, cur = LeeDBManager.makeConCur()

            sql ="delete dec03_seller where s_no = %d" % no
            cur.execute(sql)          
            if cur.rowcount == 1:
                con.commit()
                return {"result": " 삭제 성공"}
            return {"result": " 삭제 실패"}
        except Exception as e:
            print(e)
            return None
        finally:
            LeeDBManager.closeConCur(con, cur)
    def getUpdate(self,no,name,addr):
        no = int(no)
        try:
            con, cur = LeeDBManager.makeConCur()
            sql ="UPDATE dec03_seller SET s_name='%s',s_addr='%s' where s_no = %d" % (name,addr,no)
            cur.execute(sql)          
            if cur.rowcount == 1:
                con.commit()
                return {"result": " 수정 성공"}
            return {"result": " 수정 실패"}
        except Exception as e:
            print(e)
            return None
        finally:
            LeeDBManager.closeConCur(con, cur)

    



    def setAllSellerCount(self):
        try:
            con, cur = LeeDBManager.makeConCur()

            sql = "SELECT count(*) FROM dec03_seller"
            cur.execute(sql)

            for c in cur:
                self.allSellerCount = c[0]

        except Exception as e:
            print(e)
            return None
        finally:
            LeeDBManager.closeConCur(con, cur)

    def get(self, pageNo):
        try:
            con, cur = LeeDBManager.makeConCur()

            pageCount = ceil(self.allSellerCount / self.sellerPerPage)

            pageNo = int(pageNo)
            start = (pageNo - 1) * self.sellerPerPage + 1
            end = pageNo * self.sellerPerPage
           
            sql ="SELECT * FROM (SELECT rownum AS rn,s_no,s_name,s_birthday,s_addr FROM (SELECT * FROM dec03_seller ORDER BY s_no DESC)) WHERE rn>= %d AND rn<=%d" % (start,end)
     

            cur.execute(sql)
          
            sellers = []
          
            for rn, no, name, bd, addr in cur:
                bd = datetime.strftime(bd, "%Y/%m/%d")
                sellers.append({"no": no, "name": name, "bd": bd, "addr": addr})
            result = {"pageCount": pageCount, "sellers": sellers}
    
            return result
        except Exception as e:
            print(e)
            return None
        finally:
            LeeDBManager.closeConCur(con, cur)

    def reg(self, n, b, a):
 
        try:
            con, cur = LeeDBManager.makeConCur()
            sql = "INSERT INTO dec03_seller"
            sql += " VALUES (dec03_seq.nextval,"
            sql += "'%s',to_date('%s','YYYY-MM-DD'),'%s')" % (n, b, a)
            print(sql)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allSellerCount += 1
                return {"result": n + " 등록 성공"}
            return {"result": n + " 등록실패"}

        except Exception as e:
            print(e)
            return {"result": n + " 등록실패"}
        finally:
            LeeDBManager.closeConCur(con, cur)

