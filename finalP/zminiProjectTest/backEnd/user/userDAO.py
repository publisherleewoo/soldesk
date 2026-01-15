from datetime import datetime, timedelta, timezone
from os import remove
from uuid import uuid4
import jwt
from oracledb import connect

class userDAO:
    def __init__(self):

        pass

    def bye(self, memberToken):
        try:
            member = jwt.decode(memberToken, "abcd", "HS256")
            id = member['id']
            print(id)
            try:
                con = connect("leewoo/3214@195.168.9.198:1521/xe")
                cur = con.cursor()
                sql = "delete dec_miniproject where d_id='%s'" %( id)
                cur.execute(sql) 
                if(cur.rowcount ==1):
                    con.commit()        
                    return {'msg':'유저삭제완료'}
                return {'msg':'유저삭제실패'}                
            except Exception as e:
                print(e)
                return {'msg':'유저삭제db에러'}
            finally:
                cur.close()
                con.close()   
        
        except jwt.ExpiredSignatureError:
            return {"msg": "만료"}
        except jwt.DecodeError:
            return {"msg": "정보없음"}

    def idcheck(self, id):
        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = "select count(*) from dec_miniproject where d_id='%s'" % (id)
            cur.execute(sql)
            for i in cur:
                if i[0] >= 1:
                    return {"msg": "이미 존재하는 아이디입니다"}
            return {"msg": "사용가능한 아이디입니다"}

        except Exception as e:
            print(e)
            return {"msg": "에러"}
        finally:
            cur.close()
            con.close()

    def tokenCheck(self, memberToken):
        try:
            jwt.decode(memberToken, "abcd", "HS256")
            return {"msg": "activeToken"}
        except jwt.ExpiredSignatureError:
            return {"msg": "만료"}
        except jwt.DecodeError:
            return {"msg": "정보없음"}

    async def updateInfo(
        self,
        files,
        id,
        pwd,
        newPwd,
        name,
        birthday,
        postCode,
        addr,
    ):

        try:
            con = connect("leewoo/3214@195.168.9.198:1521/xe")
            cur = con.cursor()
            sql = "select * from dec_miniproject where d_id='%s' AND d_pwd='%s'" % (
                id,
                pwd,
            )
            print(sql)
            cur.execute(sql)
            if cur.fetchone():
                print("일치함")
                binaryCode = await files.read()
                if len(binaryCode) > 1024 * 1024 * 10:
                    return {"msg": "이미지 용량이 너무 큽니다"}
                try:
                    filename = files.filename
                    filetype = filename[-4:]
                    filename = (
                        filename.replace(filetype, "") + "_" + str(uuid4()) + filetype
                    )
                    f = open("./user/images/" + filename, "wb")
                    f.write(binaryCode)
                    f.close()

                    sql = (
                        "update dec_miniproject set d_pwd='%s', d_name='%s', d_postcode='%s', d_birth=to_date('%s','YYYY-MM-DD'),d_addr='%s',d_filename='%s' where d_id='%s'"
                        % (newPwd, name, postCode, birthday, addr, filename, id)
                    )
                    print(sql)
                    cur.execute(sql)

                    if cur.rowcount == 1:
                        con.commit()
                        return {"msg": "업데이트 성공"}
                except Exception as e:
                    print(e)
                    remove("./user/images/" + filename)
                    return {"msg": "업데이트가 되지 않았습니다"}

            else:
                return {"msg": "기존 비밀번호가 일치하지 않음"}
        except Exception as e:
            print(e)
        finally:
            cur.close()
            con.close()

    def getInfo(self, member):
        try:
            result = jwt.decode(member, "abcd", "HS256")

            member = {
                "id": result["id"],
                "name": result["name"],
                "postcode": result["postcode"],
                "birth": result["birth"],
                "addr": result["addr"],
                "filename": result["filename"],
            }
            return {"msg": "activeToken", "member": member}
        except jwt.ExpiredSignatureError:
            return {"msg": "만료"}

        except jwt.DecodeError:
            return {"msg": "정보없음"}

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

    def getFile(self, filename):
        return "./user/images/" + filename

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
                        "exp": datetime.now(timezone.utc) + timedelta(seconds=2700),
                    }
                    memberToken = jwt.encode(member, "abcd", "HS256")
                    return {
                        "msg": "로그인 성공",
                        "memberToken": memberToken,
                        "member": {
                            "id": id,
                            "name": name,
                            "postcode": postcode,
                            "birth": member["birth"],
                            "addr": addr,
                            "filename": filename,
                        },
                    }
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


# def signInExpRefresh(self, member):
#     try:
#         member = jwt.decode(member, "abcd", "HS256")
#         member = {
#             "id": member["id"],
#             "pwd": member["pwd"],
#             "name": member["name"],
#             "postcode": member["postcode"],
#             "birth": member["birth"],
#             "addr": member["addr"],
#             "filename": member["filename"],
#             "sysdate": member["sysdate"],
#             "exp": datetime.now(timezone.utc) + timedelta(seconds=10),
#         }
#         member = jwt.encode(member, "abcd", "HS256")

#         return {"msg": "갱신완료", "member": member}
#     except jwt.ExpiredSignatureError:
#         return {"msg": "만료"}

#     except jwt.DecodeError:
#         return {"msg": "정보없음"}
