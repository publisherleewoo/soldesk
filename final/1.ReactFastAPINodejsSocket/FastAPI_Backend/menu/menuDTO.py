from math import ceil
from tkinter import EXCEPTION
from oracledb import connect


class MenuDTO:
    def __init__(self):
        pass

    def regMenu(self, name, price, desc):

        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = "INSERT INTO dec17_menu VALUES ('%s',%s,'%s')" % (name, price, desc)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return {"msg": "등록성공"}
            return {"msg": "등록실패"}

        except Exception as e:
            print(e)
            return {"msg": "등록에러"}
        finally:
            cur.close()
            con.close()

    def allMenuCount(self):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = "SELECT count(*) FROM dec17_menu"
            cur.execute(sql)
            for c in cur:
                return c[0]
        except Exception as e:
            print(e)
        finally:
            cur.close()
            con.close()

    def getMenu(self, pageNo):
        pageNo = int(pageNo)
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            showPage = 3
            start = showPage * pageNo - (showPage - 1)
            end = showPage * pageNo
            print(start)
            print(end)
            sql = (
                "SELECT *  FROM (SELECT rownum AS rn,m_name,m_price,m_desc FROM (SELECT * FROM dec17_menu ORDER BY m_name ASC)) WHERE %s<=rn AND rn<=%s"
                % (start, end)
            )

            cur.execute(sql)

            allCount = self.allMenuCount()
            allPageCount = ceil(allCount / showPage)  # 페이지 갯수

            Menus = []
            for _, name, price, desc in cur:
                Menus.append({"n": name, "p": price, "d": desc})

            return {
                "allPageCount": allPageCount,
                "Menus": Menus,
            }

        except Exception as e:
            print(e)
        finally:
            cur.close()
            con.close()

    def deleteMenu(self, name):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = "DELETE dec17_menu WHERE m_name='%s'" % (name)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return {"msg": "삭제성공"}
            return {"msg": "삭제실패"}
        except Exception as e:
            print(e)

            return {"msg": "삭제에러"}
        finally:
            cur.close()
            con.close()
