f = open("C:/PythoneWorkspace/PythonPart1/fileWrite/snack.csv", "r", encoding="utf-8")

nameArr = []
priceArr = []
weightArr = []

for index, line in enumerate(f.readlines()):
    # print(line.strip())
    line = line.replace("\n", "")

    if index % 3 == 0: #이름
        nameArr.append(line)
    elif index % 3 == 1:#가격
        priceArr.append(line)
    elif index %3 == 2: #무게
        weightArr.append(line)

print(nameArr)
print(priceArr)
print(weightArr)


class Snack:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = int(price)
        self.weight = weight
        print(type(self.price))
    def printInfo(self):
        print(
            self.name,
            self.price,
            self.weight,
        )
        

# 객체화하여 배열에 담기
snacks = []
for index, value in enumerate(nameArr):
    s = Snack(nameArr[index], priceArr[index], weightArr[index])
    snacks.append(s)

#출력
for value in snacks:
    value.printInfo()

#가격 비싼순으로 출력    
# sortSnack = sorted(
#     snacks,
#     key=lambda snack: print(snack)
# )

# print(sortSnack)
 