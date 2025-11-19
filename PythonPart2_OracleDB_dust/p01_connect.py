# 노트북에서 작업중인 Python 프로그램
# OracleDB서버  
# 컴퓨터 통신
#  실시간 : socket통신 카톡통신 게임 등등
#  안실시간 : http통신, DB통신 등등  db 메이커들 마다 표준화된 통신방식이 없음.
#  반대로 디비메이커에서 라이브러리로 가져다 쓰라고 만들어 뒀음. 
##################################
# cx_Oracle.py(구버전) : cx_Oracle.py + instantclient
# oracledb.py (신버전) :  instantclient가 따로 없어도 되는데
#   포함된 ic가 OracleDB 구버전 지원 x 
# 구버전 oracleDB랑 연결하려면 따로 instantclient 있어야

# pip install oracledb
from oracledb import connect

# 학원 ip주소가 바뀌므로 항시체크
con = connect("leewoo/3214@195.168.9.53:1521/xe")
print(con)

con.close()