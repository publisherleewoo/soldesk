from oracledb import connect

from lee.leeDBManager import LeeDBManager
 
class Doctor:
    def calculate(guest):
        con,cur=LeeDBManager.makeConCur("leewoo/3214@195.168.9.53:1521/xe")
        # con = connect("leewoo/3214@195.168.9.53:1521/xe")

        guest.height /= 100
        guest.bmi = guest.weight / (guest.height * guest.height)

        if guest.bmi >= 39:
            guest.result = "고도비만"
        elif guest.bmi >= 32:
            guest.result = "중도비만"
        elif guest.bmi >= 30:
            guest.result = "경도비만"
        elif guest.bmi >= 24:
            guest.result = "과체중"
        elif guest.bmi >= 10:
            guest.result = "정상"
        else:
            guest.result = "저체중"

        sql = "insert into nov10_bmi values ('%s',%.2f,%1.f,%2.f,'%s')" % (
            guest.name,
            guest.height,
            guest.weight,
            guest.bmi,
            guest.result,
        )

        # cur=con.cursor()
        cur.execute(sql)
        con.commit()
        LeeDBManager.closeConCur(con,cur)
        # cur.close()
        # con.close()
