# Snack  DTO

from lee.leeDBManager import LeeDBManager


class CompanyDAO:
    def reg(company):
        con, cur = LeeDBManager.makeConCur("leewoo/3214@195.168.9.68/xe")
        sql = "insert into nov07_company values ('%s','%s','%s',%d)" % (
            company.name,
            company.addr,
            company.ceo,
            company.emp,
        )
        cur.execute(sql)

        if cur.rowcount == 1:
            con.commit()
            LeeDBManager.closeConCur(con, cur)
            return "등록성공"
        else:
            LeeDBManager.closeConCur(con, cur)
            return "등록실패"

    # def inputSql(snack):
    #     con,cur=LeeDBManager.makeConCur("leewoo/3214@195.168.9.53:1521/xe")
    #     sql = "insert into nov07_snack values (nov07_snack_seq.NEXTVAL,'%s',%d,%.2d,'%s','%s')" % (
    #         snack.name,
    #         snack.price,
    #         snack.weight,
    #         snack.exp,
    #         snack.s_c_name
    #     )

    #     cur.execute(sql)
    #     con.commit()
    #     LeeDBManager.closeConCur(con,cur)
