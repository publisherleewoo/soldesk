# from random import randint

# class Game:
#     def __init__(self):
#         self.count = 0
#         self.flag = True
#         self.ran = self.pickGameAns()

#     def getUserAns(self):
#         userAns = int(input("뭐 :"))
#         if 0 < userAns < 10001:
#             self.count += 1
#             return userAns
#         return self.getUserAns()

#     def pickGameAns(self):
#         return randint(1,10000)

#     def judge(self,gameAns,userAns):

#         if userAns > gameAns:
#             print("입력하신 숫자가 큽니다 down하시오")
#         elif userAns < gameAns:
#             print("입력하신 숫자가 작습니다 up하시오")
#         else:
#             print(self.count, "번만에 맞춤")
#             return False
#         return True

# game = Game()

# while game.flag:
#     inputNum = game.getUserAns()
#     flag = game.judge(game.ran,inputNum)


# from random import randint


# class Friend:
#     def ask(self, user):
#         print("실행")
#         userAnsTemp = user.tell()
#         if 0< userAnsTemp < 100001:
#             return userAnsTemp
#         return self.ask(user)

#     def judge(self,gameAns,userAns):
#         if gameAns == userAns:
#             print("정답!")
#             return True
#         elif gameAns > userAns:
#             print("UP")
#             return False
#         else:
#             print("DOWN")
#             return False

#     def tellResult(self,turn):
#         print("%d턴만에 정답" % turn)

#     def thinkAns(self):
#         return randint(1, 10000)

#     def start(self, user):
#         turn = 0
#         gameAns = self.thinkAns()
#         print(gameAns)
#         while True:
#             turn+=1
#             userAns = self.ask(user)
#             if self.judge(gameAns,userAns):
#                 break
#         self.tellResult(turn)

# class User:
#     def tell(self):
#         return int(input("뭐:"))


# ########
# # 1) 친구가 앉아있다가 게임하고싶어짐 -> 나를 불러서
# # 2) 친구/나 앉아있는데 친구가 게임하고 싶어져서
# friend = Friend()
# user = User()
# friend.start(user)

# # 3) 나/ 앉아있는데 게임하고싶어짐 -> 친구를 불러서
# # ...


# from random import randint
# ########################################


# class Game:
#     handTable = [None, "가위", "바위", "보"]

#     def __init__(self):
#         self.printRule(self.handTable)

#     def printRule(self,handTable):
#         for i, v in enumerate(handTable):
#             if i != 0:
#                 print("%d. %s" % (i, v))
#         print("-----")

#     def userFire(self):
#         userHand = int(input("뭐 : "))
#         if 0 < userHand < 4:
#             return userHand
#         return self.userFire()

#     def comFire(self):
#      return randint(1, 3)

#     def printHand(self,comHand, userHand):
#         print("컴 : %s" % self.handTable[comHand])
#         print("나 : %s" % self.handTable[userHand])

#     def judge(self,comHand, userHand):
#         t = userHand - comHand
#         if t == 0:
#             print("무")
#             return 0
#         elif t == -1 or t == 2:
#             print("패")
#             return 346345423
#         else:
#             print("승")
#             return 1

# game = Game()
# win = 0
# while True:
#     userHand = game.userFire()
#     comHand = game.comFire()
#     game.printHand(comHand, userHand)
#     result = game.judge(comHand, userHand)
#     if result == 346345423:
#         print("%d연승" % win)
#         break
#     win += result
#     print("-----")


# from random import randint


# class Computer:

#     def __init__(self):
#         self.start()

#     def start(self):
#         self.turn = 0
#         self.handTable=[0,"가위","바위","보"]
#         self.printRule(self.handTable)
#         self.judge(self.comRan(),User.tell())


#     def printRule(self,handTable):
#          for i, v in enumerate(handTable):
#             if i != 0:
#                 print("%d. %s" % (i, v))

#     def judge(self,comHand, userHand):
#         self.turn +=1
#         t = userHand - comHand
#         print("judge함수 안에서 turn의 수",self.turn)
#         if t == 0:
#             print("무")
#             return self.start()
#         elif t == -1 or t == 2:
#             print("패, 턴의 수 ",self.howTurn())

#             return 346345423
#         else:
#             print("승")
#             return self.start()


#     def comRan(self):
#         return randint(1,4)

#     def howTurn(self):
#         return self.turn

# class User:
#     def tell():
#         userHand = int(input("뭐 : "))
#         if 0 < userHand < 4:
#             return userHand
#         return User.tell()

# #################
# computer = Computer()
# user=User()


from random import randint
 
 
class Referee:
    def __init__(self):
        self.ruleBook = [None, "가위", "바위", "보"]
 
    def blueFire(self, blue):
        return blue.fire()
 
    def callBlueCorner(self):
        return Friend()
 
    def callRedCorner(self):
        return Player()
 
    def judge(self, bluePaper, redPaper):
        t = redPaper - bluePaper
        if t == 0:
            print("무")
            return 0
        elif t == -1 or t == 2:
            print("패")
            return -999
        else:
            print("승")
            return 1
 
    def redFire(self, red):
        redTemp = red.fire()
        if 0 < redTemp < 4:
            return redTemp
        return self.redFire(red)
 
    def tellHand(self, bluePaper, redPaper):
        print("컴 : %s" % self.ruleBook[bluePaper])
        print("나 : %s" % self.ruleBook[redPaper])
 
    def tellResult(self, win):
        print("%d연승" % win)
 
    def tellRule(self):
        for i, v in enumerate(self.ruleBook):
            if i != 0:
                print("%d) %s" % (i, v))
        print("-----")
 
    def start(self):
        blue = self.callBlueCorner()
        red = self.callRedCorner()
        self.tellRule()
        win = 0
        while True:
            bluePaper = self.blueFire(blue)
            redPaper = self.redFire(red)
            self.tellHand(bluePaper, redPaper)
            t = self.judge(bluePaper, redPaper)
            if t == -999:
                break
            win += t
            print("-----")
        self.tellResult(win)
 
 
class Friend:
    def fire(self):
        return randint(1, 3)
 
 
class Player:
    def fire(self):
        return int(input("뭐 : "))
 
 
#################
r = Referee()
r.start()
 