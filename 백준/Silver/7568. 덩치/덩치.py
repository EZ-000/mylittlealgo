import sys
input = sys.stdin.readline

N = int(input())
ws = []
hs = []

for i in range(N):
    w, h = map(int, input().split())
    ws += [w]
    hs += [h]

rank = []
for i in range(N):
    cnt = 0
    for j in range(N):
        if ws[i] < ws[j] and hs[i] < hs[j]:
            cnt += 1
    rank += [cnt + 1]

print(*rank)
