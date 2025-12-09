
from oracledb import connect


class ProductDTO:
    def getProductAll(self):
        try:
            con = connect('leewoo/3214@195.168.9.198:1521/xe')
            cur = con.cursor()
            sql = 'select * from dec09_product'
            cur.execute(sql)
            product=[]
            for name,price in cur:
                product.append({'name':name,'price':price})
            return product
        except Exception as e:
            print(e)
            return {'result':'실패'}
        finally:
            cur.close()
            con.close()

    def reg(self,name,price):
        try:
            con = connect('leewoo/3214@195.168.9.198:1521/xe')
            cur = con.cursor()
            sql = "insert into dec09_product values ('%s',%s)"%(name,price)
            cur.execute(sql)
            if (cur.rowcount ==1):
                con.commit()
                return {'result':'등록 성공'}
            return {'result':'등록 실패'}

        except Exception as e:
            print(e)
            return {'result':'등록 실패'}
        finally:
            cur.close()
            con.close()
