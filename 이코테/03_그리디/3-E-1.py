# 거스름돈
N = int(input())

answer = 0
coins = [500, 100, 50, 10]

for coin in coins:
    answer += N // coin
    N %= coin

print(answer)
