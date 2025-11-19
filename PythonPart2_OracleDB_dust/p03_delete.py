from oracledb import connect

# 학원 ip주소가 바뀌므로 항시체크
con = connect("leewoo/3214@195.168.9.53:1521/xe")

c_name = input("이름 : ")

# SQL을 str로(;빼고)
sql = "delete from nov07_company where c_name = '%s'" % (c_name)

# DB관련 작업들 다 총괄처리해주는 매니저 객체 겸 결과
cur = con.cursor()
# str로 써놓은 SQL을 DB서버로 전송 + 원격실행 + 결과받아오기
cur.execute(sql)

# commit : 실제 db서버에 반영
# -> DBeaver가 자동 commit

if cur.rowcount == 1:
    print("삭제 성공")
    con.commit()
else:
    print("삭제 실패")

cur.close()

# 연결해제
con.close()
