import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

cnt = 0
for coin in coins[::-1]:
    temp = K // coin
    if 0 < temp:
        cnt += temp
        K -= temp * coin
print(cnt)
