def row(r, c):
    while True:
        if M - 1 < c:
            break
        elif floor[r][c] == '|':
            break
        else:
            visited[r][c] = 1
        c += 1
    return r, c


def col(r, c):
    while True:
        r += 1
        if N - 1 < r:
            break
        elif floor[r][c] == '-':
            break
        else:
            visited[r][c] = 1
    return r, c


N, M = map(int, input().split())
floor = []
for _ in range(N):
    floor.append(input())

visited = [[0] * M for _ in range(N)]
cnt = 0
for n in range(N):
    for m in range(M):
        if not visited[n][m]:
            cnt += 1
            if floor[n][m] == '-':
                row(n, m)
            elif floor[n][m] == '|':
                col(n, m)
print(cnt)
