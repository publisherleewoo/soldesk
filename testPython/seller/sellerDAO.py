from math import ceil

from oracledb import connect

from seller.seller import Seller

# 1) 데이터의 총갯수
# 2) 데이터의 총갯수를 가져와서 게시판에 보여줄만큼의 숫자로 나누기
# 3) 나눈 값의 반올림을 한것이 게시판의 갯수

# 4) 페이지는  3n-2,  
#  1~3      1,4,7 = 3n-2
#  4~6      3,6,8 = 3n 인데  8일경우 3n이 아님.  그러므로  입력한 페이지값과  db에서 가져온 게시판의 갯수가 같다면
#  7~8      마지막페이지는  self.allSellerCount로 넣음
class SellerDAO:
 
    def __init__(self):
        self.setAllSellerCount()
        self.sellerPerPage= 3

    def get(self, pageNo):
        try:
            con= connect("leewoo/3214@195.168.9.68/xe")
            cur = con.cursor()
            sql ="select count(*) from nov11_seller"

            pageNo = int(pageNo)        
            start = (pageNo - 1) * self.sellerPerPage + 1   
            end = pageNo * self.sellerPerPage   

            if pageNo == self.getPageCount():     
                end = self.allSellerCount       

            sql = (
                "SELECT * from(SELECT rownum AS rn,s_no,s_name,s_addr,s_birthday FROM (SELECT * FROM nov11_seller ORDER BY s_name)) WHERE rn>=%d AND rn<=%d"
                % (start, end)
            )

            cur.execute(sql)
 
            sellers = []
            for _,no, name, addr, birthday in cur:
                s = Seller(no, name, addr, birthday)
                sellers.append(s)

            return sellers

        except Exception as e:
            print(e)
            return None
        finally:
            cur.close()
            con.close()


    def getPageCount(self):
        print(self.sellerPerPage)
        return ceil(self.allSellerCount/self.sellerPerPage)
    
    def setAllSellerCount(self): # 데이터의 총 갯수
        try:
            con= connect("leewoo/3214@195.168.9.68/xe")
            cur = con.cursor()
            sql ="select count(*) from nov11_seller"
            cur.execute(sql)
          
            for result in cur:
                print("데이터의 총갯수",result)
                self.allSellerCount= result[0]

        except Exception as e:
            print(e)
        finally:
            cur.close()
            con.close()