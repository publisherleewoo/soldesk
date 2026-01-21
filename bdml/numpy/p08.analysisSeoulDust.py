# from oracledb import connect
# import numpy as np

# try:
#     con = connect('leewoo/3214@195.168.9.198/xe')
#     cur = con.cursor()
#     sql = 'select sd_msrste_nm,avg(sd_pm10+sd_pm25) from seoul_dust group by sd_msrste_nm order by avg(sd_pm10+sd_pm25) desc'
#     cur.execute(sql)

#     dustList =[]
#     # [datetime.datetime(2025, 11, 19, 13, 30, 3), '도심권', '중구', 23, 12, '보통']
#     for a in cur:
#         dustList.append(list(a))

#     print(dustList)

# except Exception as e:
#     print(e)
# finally:
#     cur.close()
#     con.close()


from oracledb import connect
import numpy as np

# try:
#     con = connect("leewoo/3214@195.168.9.198/xe")
#     cur = con.cursor()
#     sql = "select* from seoul_dust"
#     cur.execute(sql)

#     column_name = [col[0] for col in cur.description]
#     dustList = []
#     # [datetime.datetime(2025, 11, 19, 13, 30, 3), '도심권', '중구', 23, 12, '보통']
#     for a in cur:
#         dustList.append(list(a))

#     f = open("./subwat.csv", "w", newline="", encoding="utf-8-sig")
#     f.write(",".join(column_name) + "\n")

#     for row in dustList:
#         str_row = []
#         for item in row:
#             str_row.append(str(item))
#         line = ",".join(str_row)
#         f.write(line + "\n")

#     print("CSV 저장완료")


# except Exception as e:
#     print(e)
# finally:
#     cur.close()
#     con.close()

 
  
 
