from oracledb import connect

# 학원 ip주소가 바뀌므로 항시체크
con = connect("leewoo/3214@195.168.9.53:1521/xe")

# 데이터 확보

# SQL(;빼고)
sql = "SELECT avg(s_price) FROM nov07_snack"

# DB관련작업 총괄 객체 겸 결과
cur = con.cursor()

# 실행
cur.execute(sql)

for result in cur:
    print(result[0])
    print('---------')

cur.close()
con.close()