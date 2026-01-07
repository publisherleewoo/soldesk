from datetime import datetime
from math import ceil
from oracledb import connect


class BoardDAO:
    def __init__(self):
        pass

    def deleteBoard(self, boardNo):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = ("DELETE dec_miniproject_board  WHERE db_displayno=%s") % (boardNo)

            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return {"msg": "삭제 성공"}
            return {"msg": "삭제 실패"}
        except Exception as e:
            print(e)
            return {"msg": "db 삭제 오류"}
        finally:
            cur.close()
            con.close()

    def updateBoard(self, boardNo, title, content):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = (
                "UPDATE dec_miniproject_board SET db_title='%s', db_content='%s' WHERE db_displayno=%s"
                % (title, content, boardNo)
            )
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return {"msg": "업데이트 성공"}
            return {"msg": "업데이트 실패"}
        except Exception as e:
            print(e)
            return {"msg": "db 업데이트 오류"}
        finally:
            cur.close()
            con.close()

    def postBoard(self, id, title, content):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = (
                "insert into dec_miniproject_board values ((SELECT NVL(MAX(db_displayno), 0) + 1 FROM dec_miniproject_board),'%s','%s','%s',sysdate)"
                % (title, content, id)
            )
            print(sql)
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return {"msg": "등록완료"}
            return {"msg": "등록실패"}
        except Exception as e:
            print(e)
            return {"msg": "DB 오류"}
        finally:
            cur.close()
            con.close()

    def getBoard(self, nowPageNo):
        nowPageNo = int(nowPageNo)
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")

            showPage = 5  # 보여줄 데이터 갯수

            cur = con.cursor()
            cur.execute("select count(*) from dec_miniproject_board")
            allCount = None
            for i in cur:
                allCount = i[0]
            allPage = ceil(allCount / showPage)  # 전체 페이지 개수
 

            cur = con.cursor()
            sql = (
                "SELECT * FROM (SELECT A.db_displayno, A.db_title, A.db_content, A.db_writer, A.db_date, B.d_filename,ROWNUM AS r FROM ( SELECT * FROM dec_miniproject_board ORDER BY db_displayno DESC) A LEFT JOIN dec_miniproject B ON A.db_writer = B.d_id) WHERE %s<=r AND r<=%s"
                % (5 * nowPageNo - 4, 5 * nowPageNo)
            )

            cur.execute(sql)
            boards = []
            for no, title, content, writer, date, img,r in cur:
                date = datetime.strftime(date, "%Y-%m-%d")
                boards.append(
                    {
                        "no": no,
                        "title": title,
                        "content": content,
                        "writer": writer,
                        "date": date,
                        "img": img,
                    }
                )
            return {"msg": "성공", "boards": boards, "allPage": allPage}
        except Exception as e:
            print(e)
            return {"msg": "실패"}
        finally:
            cur.close()
            con.close()
