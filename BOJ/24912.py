import sys
input = sys.stdin.readline

N = int(input())
colors = list(map(int, input().split()))

if colors[0] == 0:
    paint = [1, 2, 3]
    colors[0] = paint[0]
if colors[-1] == 0:
    paint = [1, 2, 3]
    colors[-1] = paint[0]

flag = 0
for i in range(1, N - 1):
    if colors[i] == 0:
        temp = [colors[i - 1], colors[i + 1]]
        for j in range(1, 4):
            if j not in temp:
                colors[i] = j
                break
    elif colors[i - 1] == colors[i] or colors[i] == colors[i + 1]:
        flag = 1
        break

result = [-1] if flag == 0 else colors
print(*result)
