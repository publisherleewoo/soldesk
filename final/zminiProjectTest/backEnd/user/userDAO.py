from datetime import datetime, timedelta, timezone
from os import remove
from uuid import uuid4
from fastapi.responses import FileResponse
import jwt
from oracledb import connect


class userDAO:
    def __init__(self):
        pass

    async def signUp(
        self,
        files,
        id,
        pwd,
        name,
        postCode,
        birthday,
        addr,
    ):
        try:
            binaryCode = await files.read()
            maxSize = 1024 * 1024 * 10
            print(len(binaryCode))
            print(maxSize)
            if len(binaryCode) > maxSize:
                return {"msg": "이미지 용량이 너무 큽니다"}
            fileName = files.filename
            fileType = fileName[-4:]
            filename = fileName.replace(fileType, "") + "_" + str(uuid4()) + fileType
            f = open("./user/images/" + filename, "wb")
            f.write(binaryCode)
            f.close()

        except Exception as e:
            print(e)
            return {"msg": "이미지 등록 실패"}
        finally:
            try:
                con = connect("leewoo/3214@195.168.9.198:1521/xe")
                cur = con.cursor()
                sql = (
                    "INSERT INTO dec_miniproject VALUES ('%s','%s','%s',%s,to_date('%s','YYYY-MM-DD'),'%s','%s',sysdate)"
                    % (
                        id,
                        pwd,
                        name,
                        postCode,
                        birthday,
                        addr,
                        filename,
                    )
                )
                print(sql)
                cur.execute(sql)
                if cur.rowcount == 1:
                    con.commit()
                    return {"msg": "등록 성공"}
                return {"msg": "등록 실패"}
            except Exception as e:
                remove("./user/images/" + filename)  # 가입 실패시에 이미지 삭제
                print(e)
                return {"msg": "DB 등록 실패"}
            finally:
                cur.close()
                con.close()

    def signInExpRefresh(self, member):
        try:
            member = jwt.decode(member, "abcd", "HS256")
            member = {
                "id": member["id"],
                "pwd": member["pwd"],
                "name": member["name"],
                "postcode": member["postcode"],
                "birth": member["birth"],
                "addr": member["addr"],
                "filename": member["filename"],
                "sysdate": member["sysdate"],
                "exp":datetime.now(timezone.utc)+timedelta(seconds=10)
            }
            member=jwt.encode(member,'abcd','HS256')

            return {'msg':'갱신완료','member':member}
        except jwt.ExpiredSignatureError:
            return {"msg": "만료"}
      
        except jwt.DecodeError:
            return {"msg": "정보없음"}
      

    def getFile(self,filename):
        return './user/images/'+filename

    def login(self, id, inputPwd):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = "SELECT * FROM dec_miniproject WHERE d_id='%s'" % (id)
            cur.execute(sql)

            count = 0
            for id, pwd, name, postcode, birth, addr, filename, sysdate in cur:
                count += 1
                if inputPwd == pwd:
                    member = {
                        "id": id,
                        "pwd": pwd,
                        "name": name,
                        "postcode": postcode,
                        "birth": datetime.strftime(birth, "%Y-%m-%d"),
                        "addr": addr,
                        "filename": filename,
                        "sysdate": datetime.strftime(sysdate, "%Y-%m-%d"),
                        "exp": datetime.now(timezone.utc) + timedelta(seconds=10),
                    }
                    member = jwt.encode(member, "abcd", "HS256")
                    return {"msg": "로그인 성공", "member": member, "id": id}
                else:
                    return {"msg": "로그인 실패(pwd)"}
            if count == 0:
                return {"msg": "로그인 실패(미가입ID)"}

            return {"msg": "로그인 값이 없습니다"}
        except Exception as e:
            print(e)
            return {"msg": "로그인 DB 에러"}

        finally:
            cur.close()
            con.close()

    def delete(self, id, pwd):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = "DELETE dec_miniproject WHERE d_id='%s' AND d_pwd='%s'" % (id, pwd)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return {"msg": "삭제 성공"}
            return {"msg": "삭제 실패"}
        except Exception as e:
            print(e)
            return {"msg": "삭제 에러"}
        finally:
            cur.close()
            con.close()
