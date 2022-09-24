import sys
input = lambda: sys.stdin.readline().rstrip()

board = [input() for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == 'F':
            if (i % 2 and j % 2) or (not i % 2 and not j % 2):
                cnt += 1
print(cnt)
