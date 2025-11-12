from consoleScreen import ConsoleScreen
from seller.sellerDAO import SellerDAO


if __name__ =="__main__":
    sellerDAO=SellerDAO()
    menu = ConsoleScreen.showMainMenu()
    
    if menu =="1":
        pageCount = sellerDAO.getPageCount()
        pageNo = ConsoleScreen.showSelectPageMenu(pageCount)
        sellers = sellerDAO.get(pageNo)
        for seller in sellers:
            print(seller.name)