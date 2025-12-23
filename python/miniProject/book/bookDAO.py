from lib.leeDB import LeeDB


class BookDAO:

    def create(self):
        self.inputCreate()

        sql = (
            "INSERT INTO nov_book VALUES ('%s',%d,'%s','%s',TO_DATE('%s','YYYY-MM-DD'))"
            % (self.name, int(self.price), self.publisher, self.author, self.pdate)
        )
        con, cur = LeeDB.dbstart()
        cur.execute(sql)
        if cur.rowcount > 0:
            con.commit()
            print("생성 성공")
        LeeDB.dbclose(con, cur)

    def inputCreate(self):
        self.name = input("책이름")
        self.price = input("책가격")
        self.publisher = input("출판사")
        self.author = input("책저자")
        self.pdate = input("출판일")

    def inputCreate2(self):
        self.price = input("책가격")
        self.publisher = input("출판사")
        self.author = input("책저자")
        self.pdate = input("출판일")

    def readAll(self):
        sql = "select * from nov_book"
        con, cur = LeeDB.dbstart()
        cur.execute(sql)
        con.commit()
        for c in cur:
            print(c)
        LeeDB.dbclose(con, cur)

    def selectInput(self):
        return input("책제목을 입력해주세요")

    def read(self):
        self.inputStr = self.selectInput()
        sql = "select * from nov_book where b_name='%s'" % (self.inputStr)
        con, cur = LeeDB.dbstart()
        cur.execute(sql)
        con.commit()
        for c in cur:
            print(c)
        LeeDB.dbclose(con, cur)

    def update(self):
        self.read()
        self.inputCreate2()

        sql = (
            "update nov_book SET b_price=%d,b_publisher='%s',b_author='%s',b_pdate=TO_DATE('%s','YYYY-MM-DD') where b_name='%s'"
        ) % (int(self.price), self.publisher, self.author, self.pdate, self.inputStr)

        print(sql)
        con, cur = LeeDB.dbstart()
        cur.execute(sql)
        if cur.rowcount > 0:
            con.commit()
            print("업데이트 성공")
        LeeDB.dbclose(con, cur)

    def delete(self):
        self.inputStr = self.selectInput()
        sql = "delete from nov_book where b_name ='%s'"%(self.inputStr)
        con, cur = LeeDB.dbstart()
        cur.execute(sql)
        if cur.rowcount > 0:
            con.commit()
            print("제거성공")
        LeeDB.dbclose(con, cur)

        