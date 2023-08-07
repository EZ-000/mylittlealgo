# 큰 수의 법칙
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

answer = 0
for i in range(1, M + 1):
    if i % 4 == 0:
        answer += arr[-2]
    else:
        answer += arr[-1]

print(answer)
