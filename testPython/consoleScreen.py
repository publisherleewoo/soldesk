class ConsoleScreen:

    def showMainMenu():
        return input("뭐 :")

    def showSelectPageMenu(pageCount):
        return input("페이지 (1~%d) :" % pageCount)