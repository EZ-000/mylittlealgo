# 큰 수의 법칙
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[-1]
second = arr[-2]

count = K * (M // (K + 1)) + (M % (K + 1))
print(first * count + second * (M - count))
