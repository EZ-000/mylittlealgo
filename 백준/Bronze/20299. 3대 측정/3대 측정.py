import sys
input = sys.stdin.readline


N, K, L = map(int, input().split())
cnt = 0
ratings = []
for _ in range(N):
    xs = list(map(int, input().split()))
    S = 0
    for x in xs:
        S += x
        if x < L:
            break
    else:
        if K <= S:
            cnt += 1
            ratings += xs
print(cnt)
print(*ratings)
