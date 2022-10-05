import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
status = [input() for _ in range(N)]

r = [0] * N
c = [0] * M
for i in range(N):
    for j in range(M):
        if status[i][j] == 'X':
            r[i] = 1
            c[j] = 1

cnt = r.count(0) if c.count(0) < r.count(0) else c.count(0)
print(cnt)
