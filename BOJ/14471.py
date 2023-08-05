import sys
input = sys.stdin.readline


N, M = map(int, input().split())
max_yen = 0
price = 0
for _ in range(M):
    A, B = map(int, input().split())
    if A < N:
        temp = N - A
        price += temp
        if max_yen < temp:
            max_yen = temp

print(price - max_yen)
