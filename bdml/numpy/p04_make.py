import numpy as np

 
print(np.zeros([2,3])) 
print(np.arange(5)) 
print(np.random.randint(1,5,[3,2]))





# # DB/객체list/Pandas

# # 1) 후속기술들이 NUmPy를 써서
# # 2) 인공신경망(사실은 행렬게산)
# #   행렬이 list -> 쌩list보다는 np.array가 낫고
# #   인공신경망 값들은 AI찾아낼텐데, 구조는 세워줘야

# a = np.zeros([3, 2], dtype=np.int64)
# print(a)
# print()
# b = np.ones([4, 2])
# print(b)
# print("===================")
# c = np.empty([2, 3])  # 값 신경쓰지말고
# print(c)
# print("===================")
# d = np.arange(3)  # [0,1,2]  range와 비슷한개념
# print(d)
# print("===================")
# e = np.random.rand(3, 2)
# print(e)
# f = np.random.randn(3, 2)
# print(f)
# g = np.random.randint(1, 5, [3, 2])
# print(g)




