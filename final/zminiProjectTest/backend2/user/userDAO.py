from os import remove
from uuid import uuid4
from oracledb import connect


class UserDAO:
    def __init__(self):
        pass

    async def reg(self, id, pwd, name, birthday, postCode, addr, files):
        try:
            binaryCode = await files.read()
            if len(binaryCode) >= 1024 * 1024 * 10:
                return {"msg": "이미지 용량이 10mb 미만이여야 합니다."}

            filename = files.filename
            type = filename[-4:]
            filename = filename.replace(type, "") + "_" + str(uuid4()) + type
            f = open("./user/files/" + filename, "wb")
            f.write(binaryCode)
            f.close()
        except Exception as e:
            remove("./user/files/" + filename)
            print(e)
            return {'msg':"이미지 등록 실패"}
        finally:
            try:
                con = connect("leewoo/3214@195.168.9.198:1521/xe")
                cur = con.cursor()
                sql = (
                    "INSERT INTO dec_miniproject VALUES ('%s','%s','%s',%d,to_date('%s','YYYY-MM-DD'),'%s','%s',sysdate)"
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
                cur.execute(sql)
                if(cur.rowcount==1):
                    con.commit()
                    return {'msg':'DB등록성공'}
                return {'msg':'DB등록실패'}
            except Exception as e:
                print(e)
                remove("./user/files/" + filename)
            finally:
                cur.close()
                con.close()
