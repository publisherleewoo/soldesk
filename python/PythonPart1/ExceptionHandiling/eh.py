# # compiler방식 언어

# x = int(input("x: "))
# y = int(input("y: "))

# a = x+y
# b = x-y
# c = x*y
# d = x/y


# try:
#     x = int(input("x : "))
#     y = int(input("y : "))
#     z = x/y
#     print(z)
# except ZeroDivisionError:
#     print("나누기 0은 없음")
# except ValueError:
#     print("잘못 입력")
# else:
#    print("try부분 하는동안 아무 문제 없으면")
# finally:
#   print("무조건 실행하는 부분")



# class Cal:
#    x=0
#    y=0
#    def __init__(self):
#       self.x = int(input("x:"))
#       self.y = int(input("y:"))
#    def div(self):
#       try:
#         z = self.x/self.y
#       except:
#         print("뭔가잘못됨")
#       finally:
#          return int(z)
      


# cal1 = Cal()
# result = cal1.div()
# print(result)




class Calculator:
   def getMoks(x,y):
      try:
         z=x/y
         return z
      except:
         print("나누기 0?")
         return -999

x = int(input("x :"))
y = int(input("y :"))
 


 