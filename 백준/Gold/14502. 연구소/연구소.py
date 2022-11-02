import sys
from copy import deepcopy
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def bfs(v, visited):
    global max_cnt
    temp = cnt
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    que = deque(v)
    while que:
        nr, nc = que.popleft()
        for idx in range(4):
            tr = nr + dr[idx]
            tc = nc + dc[idx]
            if (0 <= tr < N) and (0 <= tc < M) and not visited[tr][tc]:
                temp -= 1
                if temp < max_cnt:
                    return
                visited[tr][tc] = 2
                que.append((tr, tc))
    max_cnt = temp


def ncr(n, r, s, arr):
    if r == 0:
        new_walls.append(comb[:])
    else:
        for idx in range(s, n - r + 1):
            comb[r - 1] = arr[idx]
            ncr(n, r - 1, idx + 1, arr)


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

walls = []
virus = []
saves = []
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            walls.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))
        else:
            saves.append((i, j))
            cnt += 1

new_walls = []
comb = [0, 0, 0]
ncr(len(saves), 3, 0, saves)

cnt -= 3
max_cnt = 0
for new_wall in new_walls:
    check = deepcopy(board)
    for i, j in new_wall:
        check[i][j] = 1
    bfs(virus, check)

print(max_cnt)
