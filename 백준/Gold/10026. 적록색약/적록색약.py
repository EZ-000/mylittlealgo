import sys
from collections import deque
from copy import deepcopy
input = lambda: sys.stdin.readline().rstrip()


def bfs(r, c, color, grid, visited):
    que = deque([(r, c)])
    while que:
        r, c = que.popleft()
        for idx in range(4):
            nr, nc = r + dr[idx], c + dc[idx]
            if (0 <= nr < N) and (0 <= nc < N) and not visited[nr][nc] and grid[nr][nc] == color:
                que.append((nr, nc))
                visited[nr][nc] = 1


def check(grid, visited):
    cnt = 0
    for row in range(N):
        for col in range(N):
            if not visited[row][col]:
                cnt += 1
                visited[row][col] = 1
                bfs(row, col, grid[row][col], grid, visited)
    return cnt


N = int(input())
grid1 = []
for _ in range(N):
    grid1.append(list(input()))

grid2 = deepcopy(grid1)
for i in range(N):
    for j in range(N):
        if grid2[i][j] == 'G':
            grid2[i][j] = 'R'

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
print(check(grid1, visited1), check(grid2, visited2))
