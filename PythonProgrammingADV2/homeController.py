from doctor import Doctor
from consoleScreen import ConsoleScreen
 
if __name__ =="__main__":
   g = ConsoleScreen.getGuestInfo()
   Doctor.calculate(g)
   ConsoleScreen.printResult(g) 

