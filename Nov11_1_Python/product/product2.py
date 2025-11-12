# 객체의 속성 : member variable, attribute, field
# DTO,VO,Bean
class Product2:
    def __init__(self, no, name, price, cate, s_name, s_addr, s_birthday):
        self.no = no
        self.name = name
        self.price = int(price)
        self.cate = cate
        self.s_name = s_name
        self.s_addr = s_addr
        self.s_birthday = s_birthday
