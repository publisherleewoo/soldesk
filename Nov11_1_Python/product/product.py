# 객체의 속성 : member variable, attribute, field
# DTO,VO,Bean
class Product:
    def __init__(self, no, name, price, cate,s_no):
        self.no = no
        self.name = name
        self.price = int(price)
        self.cate = cate
        self.s_no = int(s_no)

