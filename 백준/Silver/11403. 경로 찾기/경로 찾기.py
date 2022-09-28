import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][k] == 1 or (graph[j][i] == 1 and graph[i][k] == 1):
                graph[j][k] = 1

for row in graph:
    for col in row:
        print(col, end=' ')
    print()
