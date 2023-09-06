N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
flag = 1
count = 0
while flag:
    for offset in range(4):
        td = (d + 3 - offset) % 4
        nr, nc = r + dr[td], c + dc[td]
        if nr < 0 or N <= nr or nc < 0 or M <= nc:
            continue
        if board[nr][nc] == 0:
            count += 1
            board[nr][nc] = 2
            r, c = nr, nc
            d = td
            break
    else:
        back = (d + 2) % 4
        r, c = r + dr[back], c + dc[back]
        if board[r][c] == 1:
            flag = 0

print(count)
