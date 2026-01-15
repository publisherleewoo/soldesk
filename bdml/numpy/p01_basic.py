import numpy as np

name = np.array(["홍길동", "김길동", "이길동"])
kor = np.array([100, 90, 85])
eng = np.array([10, 50, 20])
mat = np.array([40, 60, 55])

sum = kor + eng + mat
avg = sum / 3
print(avg)

over60 = avg > 60
print(over60)
print(name[over60])  # masking1
print(name[kor == 100])

a = 15 < eng
b = eng < 60
c = a & b

print(name[c])

# &&는 and를 만나면 중간에 탈출하는 연산자이지만
# &는 끝까지 가는 연산자이다.
