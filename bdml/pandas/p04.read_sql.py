from oracledb import connect
import pandas as pd

con = connect("leewoo/3214@195.168.9.198/xe")
 
sql = "select * from seoul_dust"

d= pd.read_sql(sql,con)

print(d)

con.close()