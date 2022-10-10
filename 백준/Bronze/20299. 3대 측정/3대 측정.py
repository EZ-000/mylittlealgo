import sys
input = sys.stdin.readline


N, K, L = map(int, input().split())
cnt = 0
ratings = []
for _ in range(N):
    xs = list(map(int, input().split()))
    for x in xs:
        if x < L:
            break
    else:
        if K <= sum(xs):
            cnt += 1
            ratings += xs
print(cnt)
print(*ratings)
