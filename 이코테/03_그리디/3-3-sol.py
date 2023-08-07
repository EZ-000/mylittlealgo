N, M = map(int, input().split())

answer = 0
for _ in range(N):
    row = list(map(int, input().split()))
    answer = max(answer, min(row))

print(answer)
