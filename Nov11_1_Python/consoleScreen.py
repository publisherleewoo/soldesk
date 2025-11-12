from product.product import Product
from seller.seller import Seller


class ConsoleScreen:
    def showMainMenu():
        print("1) 판매자 등록")
        print("2) 상품 등록")
        print("3) 전체 판매자 조회")
        print("4) 전체 판매자 조회")
        print("5) 판매자 조회")
        print("6) 상품 조회")
        print("7) 판매자 검색")
        print("8) 상품 검색")
        print("9) 상품 검색")

        print("10) 종료")
        return input("뭐:")

    def showSearchMenu():
        return input("검색어 : ")

    def showSelectPageMenu(pageCount):
        return input("페이지 (1~%d) :" % pageCount)
    def showSelectPageNoMenu(pageCount):
        return input("페이지 (1~%d) :" % pageCount) 


    def showSellerRegMenu():
        name = input("판매자명 : ")
        addr = input("판매자 집 주소 : ")
        birthday = input("판매자 생일 : ")
        return Seller(None, name, addr, birthday)

    def showProductMenu():
        name = input("상품명 : ")
        price = input("상품가격 : ")
        cate = input("문구 : ")
        s_no = input("판매자 번호 : ")
        return Product(None, name, price, cate, s_no)

    def showResult(result):
        print(result)
        print("------")

    def showSellers(sellers):
        print(sellers)
        for seller in sellers:
            print(seller.no)
            print(seller.name)
            print(seller.addr)
            print(seller.birthday)
            print("------")

    def showProduct(products):
        for product in products:
            print(product.no)
            print(product.name)
            print(product.price)
            print(product.cate)
            print(product.s_no)
            print("------")
    def showProduct2(products):
        for product in products:
            print(product.no)
            print(product.name)
            print(product.price)
            print(product.cate)
            print(product.s_name)
            print(product.s_addr)
            print(product.s_birthday)
            print("------")

