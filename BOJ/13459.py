import sys
input = lambda sys.stdin.readline().rstrip()
from collections import deque


def bfs(red, blue):
    global cnt
    red_que = deque(red)
    blue_que = deque(blue)
    while True:
        if 10 < cnt:
            return 0
        cnt += 1
        red_now = red_que.popleft()
        blue_now = blue_que.popleft()
        for n in range(4):
            red_new = (red_now[0] + dr[n], red_now[1] + dr[n])
            blue_new = (blue_now[0] + dr[n], blue_now[1] + dr[n])
            while True:
                if blue_new == goal:
                    return 0
                elif red_new == goal:
                    return 1
                elif blue_new


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

for r in range(N):
    for c in range(M):
        if board[r][c] == 'R':
            R = (r, c)
        if board[r][c] == 'B':
            B = (r, c)
        if board[r][c] == '0':
            goal = (r, c)

answer = 0
cnt = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


