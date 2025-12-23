from math import ceil
from lee.leeDBManager import LeeDBManager
from seller.seller import Seller

# 메소드 첫번째 파라메타로 self를 넣냐 마냐 - static
# 멤버변수가 없다 -> 저장할게 없다 ->객체를 안만들어도 된다
# -> 객체를 안만들고도 사용가능한 static메소드


# 총 판매자 수 파악 : DB서버랑 통신해서.. ->부담스러움 ->횟수를 줄이자
# -> 처음 한번만 세고, 변화가 일어나면 수동카운팅
class SellerDAO:
    def __init__(self):
        self.setAllSellerCount()
        self.sellerPerPage = 3

    def get(self, pageNo, searchTxt):
        try:
            con, cur = LeeDBManager.makeConCur()
            searchTxt = "%" + searchTxt + "%"
            pageNo = int(pageNo)
            
            start = (pageNo - 1) * self.sellerPerPage + 1
            end = pageNo * self.sellerPerPage

            sql = "SELECT * from(SELECT rownum AS rn,s_no,s_name,s_addr,s_birthday FROM (SELECT * FROM nov11_seller where S_NAME LIKE '%s' or s_addr LIKE '%s'" % (
                searchTxt,
                searchTxt,
            ) + "ORDER BY s_name)) WHERE rn>=%d AND rn<=%d" % (
                start,
                end,
            )
            print(sql)
            cur.execute(sql)

            sellers = []
            for _, no, name, addr, birthday in cur:
                print(cur)
                s = Seller(no, name, addr, birthday)
                sellers.append(s)

            return sellers

        except Exception as e:
            print(e)
            return None
        finally:
            LeeDBManager.closeConCur(con, cur)

    def getAll(self):
        try:
            con, cur = LeeDBManager.makeConCur()
            sql = "select * from nov11_seller order by s_name"
            cur.execute(sql)

            sellers = []
            for no, name, addr, birthday in cur:
                s = Seller(no, name, addr, birthday)
                sellers.append(s)
            return sellers

        except Exception as e:
            print(e)
            return None
        finally:
            LeeDBManager.closeConCur(con, cur)

    def getPageCount(self, searchTxt):
        if searchTxt == "":
            sellerCount = self.allSellerCount
        else:
            sellerCount = self.getSellerCount(searchTxt)
        return ceil(sellerCount / self.sellerPerPage)

    def reg(self, seller):
        try:
            con, cur = LeeDBManager.makeConCur()
            sql = (
                "insert into nov11_seller VALUES (nov11_seq.nextval,'%s','%s',to_date('%s','YYYYMMDD'))"
                % (seller.name, seller.addr, seller.birthday)
            )

            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allSellerCount += 1
                print(self.allSellerCount)

                return "등록 성공"
            else:
                return "등록 실패"

        except Exception as e:
            print(e)
            return "등록 실패, 에러"
        finally:
            LeeDBManager.closeConCur(con, cur)

    def getSellerCount(self, searchTxt):
        try:
            con, cur = LeeDBManager.makeConCur()
            searchTxt = "%" + searchTxt + "%"
            sql = (
                "select count(*) from nov11_seller where S_NAME LIKE '%s' or s_addr LIKE '%s'"
                % (searchTxt, searchTxt)
            )
            cur.execute(sql)

            for result in cur:
                return result[0]

        except Exception as e:
            print(e)
            return 0
        finally:
            LeeDBManager.closeConCur(con, cur)

    def setAllSellerCount(self):
        try:
            con, cur = LeeDBManager.makeConCur()
            sql = "select count(*) from nov11_seller"
            cur.execute(sql)

            for result in cur:
                self.allSellerCount = result[0]  # allSellerCount라는 멤머변수에 셋팅

        except Exception as e:
            print(e)
        finally:
            LeeDBManager.closeConCur(con, cur)
