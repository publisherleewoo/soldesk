from product.productDAO import ProductDAO
from seller.sellerDAO import SellerDAO
from consoleScreen import ConsoleScreen

if __name__ == "__main__":

    sellerDAO = SellerDAO()
    productDAO = ProductDAO()
    sellerDAO.getPageCount("")
    productDAO.getPageCount("")
    while True:
        menu = ConsoleScreen.showMainMenu()

        if menu == "10":
            print("끝")
            break
        elif menu == "1":
            seller = ConsoleScreen.showSellerRegMenu()
            result = sellerDAO.reg(seller)
            ConsoleScreen.showResult(result)
        elif menu == "2":
            product = ConsoleScreen.showProductMenu()
            result = productDAO.reg(product)
            ConsoleScreen.showResult(result)
        elif menu == "3":
            sellers = sellerDAO.getAll()
            ConsoleScreen.showSellers(sellers)
        elif menu == "4":
            products = productDAO.getAll()
            ConsoleScreen.showProduct(products)
        elif menu == "5":
            pageCount = sellerDAO.getPageCount("")  # 총 페이지 갯수를 작성함
            pageNo = ConsoleScreen.showSelectPageMenu(
                pageCount
            )  # 입력한 페이지 개수를 갖고옴
            sellers = sellerDAO.get(pageNo, "")  # rownum으로 부분 페이지 가져옴
            ConsoleScreen.showSellers(sellers)  # 화면에 찍음
        elif menu == "6":  # 상품조회
            pageCount = productDAO.getPageCount()
            pageNo = ConsoleScreen.showSelectPageMenu(pageCount)
            products = productDAO.get(pageNo)
            ConsoleScreen.showProduct(products)
            # 총 페이지 수를 구하자
            # 1-1)총 판매자 수 구하자 :
            # 1-2)한페이지당 3명씩 보여준다 치면 총 3페이지
        elif menu == "7":  # 회사검색
            searchTxt = ConsoleScreen.showSearchMenu()
            pageCount = sellerDAO.getPageCount(searchTxt)
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageMenu(pageCount)
            sellers = sellerDAO.get(pageNo, searchTxt)
            print("sellers", sellers)
            ConsoleScreen.showSellers(sellers)
        elif menu == "8":  # 상품검색
            searchTxt = ConsoleScreen.showSearchMenu()
            pageCount = productDAO.getPageCount(searchTxt)
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageMenu(pageCount)
            products = productDAO.get(pageNo, searchTxt)
            ConsoleScreen.showProduct(products)
        elif menu == "9":  # 상품검색
            searchTxt = ConsoleScreen.showSearchMenu()
            pageCount = productDAO.getPageCount(searchTxt)
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageMenu(pageCount)
            products = productDAO.get2(pageNo, searchTxt)         
            ConsoleScreen.showProduct2(products)  
        elif menu == "11":  # 최고가 상품
            pass
            