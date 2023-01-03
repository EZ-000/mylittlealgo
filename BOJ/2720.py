import sys
input = sys.stdin.readline

coins = [25, 10, 5, 1]

T = int(input())
for _ in range(T):
    result = []
    change = int(input())
    for coin in coins:
        num = change // coin
        result.append(num)
        change -= coin * num
    print(*result)
