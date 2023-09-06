# 상하좌우
N = int(input())
plan = input().split()

direction = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
x = 1
y = 1
for letter in plan:
    nx = x + direction[letter][0]
    ny = y + direction[letter][1]
    if 0 < nx < N + 1 and 0 < ny < N + 1:
        x, y = nx, ny

print(x, y)
