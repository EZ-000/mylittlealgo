import sys
input = sys.stdin.readline

N, L, K = map(int, input().split())
scores = [0] * N
for idx in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        scores[idx] = 140
    elif sub1 <= L:
        scores[idx] = 100
scores.sort(reverse=True)
print(sum(scores[:K]))
