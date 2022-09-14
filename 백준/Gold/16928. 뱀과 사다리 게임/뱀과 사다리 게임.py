import sys
input = sys.stdin.readline

from collections import deque


N, M = map(int, input().split())
ladders = {}
snakes = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v

q = deque([1])
cnt = [0] * 101
visited = [0] * 101

while q:
    now = q.popleft()
    if now == 100:
        print(cnt[100])
        break
    for n in range(1, 7):
        move = now + n
        if move < 101 and not visited[move]:
            if move in ladders.keys():
                move = ladders[move]
            if move in snakes.keys():
                move = snakes[move]

            if not visited[move]:
                visited[move] = 1
                cnt[move] = cnt[now] + 1
                q.append(move)
