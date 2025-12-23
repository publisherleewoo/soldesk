# AOP적인 생각 : 어떤 DB작업을 하든지 공통된 부분이 존재
#               ->따로 정리 해야겠다
# 그 정리하는거 이번 프로젝트가 뿐만 아니라 앞으로 계속 사용될듯
# => DB관련 라이브러리를 만들어야겠다
from oracledb import connect


class LeeDBManager:
    def makeConCur():
        con = connect("leewoo/3214@195.168.9.74:1521/xe")  # "leewoo/3214@195.168.9.74:1521/xe"
        cur = con.cursor()
        return con, cur

    def closeConCur(con, cur):
        cur.close()
        con.close()
