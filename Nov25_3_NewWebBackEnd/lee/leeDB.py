from oracledb import connect


class LeeDB:

    def dbstart():
       con = connect("leewoo/3214@195.168.9.198:1521/xe")
       cur =con.cursor()
       return con,cur 

    def dbclose(con,cur):
       cur.close()
       con.close()