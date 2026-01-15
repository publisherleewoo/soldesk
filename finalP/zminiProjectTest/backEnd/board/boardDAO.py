from datetime import datetime
from math import ceil
from oracledb import connect


class BoardDAO:
    def __init__(self):
        self.allPostCount = None
        self.showPage = 5


    def deleteReply(self,replyNo):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = "delete dec_miniproject_board_reply where dbr_no=%s"%(replyNo)
            cur.execute(sql)
            print(sql)
            if(cur.rowcount ==1):
                con.commit()
                return {"msg":"댓글삭제성공"}
            return {"msg":"댓글삭제실패"}

        except Exception as e:
            print(e)
            return {"msg":"댓글DB삭제실패"}
        
        finally:
            cur.close()
            con.close()


    def updateReply(self,replyNo,reply):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = "update dec_miniproject_board_reply set dbr_content='%s',dbr_date=sysdate where dbr_no='%s'"%(reply,replyNo)
            cur.execute(sql)
            print(sql)
            if(cur.rowcount ==1):
                con.commit()
                return {"msg":"댓글수정성공"}
            return {"msg":"댓글수정실패"}

        except Exception as e:
            print(e)
            return {"msg":"댓글DB실패"}
        
        finally:
            cur.close()
            con.close()


    def getReply(self,postNo):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = "select * from dec_miniproject_board_reply where dbr_displayno = %s  order by dbr_no asc" %(postNo)
            cur.execute(sql)
            replys=[]
            for no,writer,content,date,_ in cur:
                date = datetime.strftime(date,'%Y-%m-%d')
                replys.append({"no":no,"writer":writer,"content":content,"date":date})
            return {'msg':'조회성공',"replys":replys}
        except Exception as e:
            print(e)
            return {'msg':'리플db조회실패'}
        finally:
            cur.close()
            con.close()

        pass
    def postReply(self, boardNo, id, reply):
        
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = "INSERT INTO dec_miniproject_board_reply VALUES ((SELECT NVL(MAX(dbr_no), 0) + 1 FROM dec_miniproject_board_reply), '%s', '%s', sysdate, '%s')" % (id, reply, boardNo)
            
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return {"msg": "댓글등록성공"}
            return {"msg": "댓글등록실패"}

        except Exception as e:
            print(e)
            return {"msg": "리플 DB 실패"}
        finally:
            cur.close()
            con.close()

    def deleteBoard(self, boardNo):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = ("DELETE dec_miniproject_board  WHERE db_displayno=%s") % (boardNo)

            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allPostCount -= 1
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

    def getInputBoard(self, str):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            cur.execute(
                "select count(*) from dec_miniproject_board WHERE db_title LIKE '%"
                + str
                + "%'"
            )

            for i in cur:
                self.allPostCount = i[0]
            allPage = ceil(self.allPostCount / self.showPage)

            cur = con.cursor()
            cur.execute(
                "SELECT * FROM (SELECT A.db_displayno, A.db_title, A.db_content, A.db_writer, A.db_date, B.d_filename,ROWNUM AS r FROM (    SELECT * FROM dec_miniproject_board     ORDER BY db_displayno DESC) A LEFT JOIN dec_miniproject B ON A.db_writer = B.d_id) WHERE db_title LIKE '%"
                + str
                + "%'"
            )

            boards = []
            for no, title, content, writer, date, file, _ in cur:
                print(no, title, content, writer, date, file)
                date = datetime.strftime(date, "%Y-%m-%d")
                boards.append(
                    {
                        "no": no,
                        "title": title,
                        "content": content,
                        "writer": writer,
                        "date": date,
                    }
                )
            return {"msg": "성공", "boards": boards, "allPage": allPage}
        except Exception as e:
            print(e)
            return {
                "msg": "실패",
            }
        finally:
            cur.close()
            con.close()

    def getBoardCountAll(self):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            cur.execute("select count(*) from dec_miniproject_board")
            for i in cur:
                self.allPostCount = i[0]

        except Exception as e:
            print(e)
            return {"msg": "getBoardCountAll db에러"}

        finally:
            cur.close()
            con.close()

    def getBoard(self, nowPageNo):
        nowPageNo = int(nowPageNo)
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")

            self.getBoardCountAll()

            allPage = ceil(self.allPostCount / self.showPage)

            cur = con.cursor()
            sql = (
                "SELECT * FROM (SELECT A.db_displayno, A.db_title, A.db_content, A.db_writer, A.db_date, B.d_filename,ROWNUM AS r FROM ( SELECT * FROM dec_miniproject_board ORDER BY db_displayno DESC) A LEFT JOIN dec_miniproject B ON A.db_writer = B.d_id) WHERE %s<=r AND r<=%s"
                % (5 * nowPageNo - 4, 5 * nowPageNo)
            )

            cur.execute(sql)
            boards = []
            for no, title, content, writer, date, img, r in cur:
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
