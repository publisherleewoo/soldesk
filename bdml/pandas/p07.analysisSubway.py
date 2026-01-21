import pandas as pd

a =pd.read_csv("../numpy/subway.csv",names=['년','월','일','호선','역','인풋','아웃풋'])
print(a)
df = pd.DataFrame(a)

print(df)

# 데이터 어떻게 생겼나  -> 마지막 데이터 3개만 보기
print(df.tail(3))

# 언제부터 모은 데이터인가 -> 첫데이터 날짜만
print(df.head(1)[["년","월","일"]])

#100~110번데이터 노선번호 역이름
print(df.iloc[100:111][["호선","역"]])


