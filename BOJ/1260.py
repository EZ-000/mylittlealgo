import sys
input = sys.stdin.readline


def dfs(start):
    stack = [start]
    visited = [0] * (N + 1)
    while stack:
        now = stack.pop()
        if not visited[now]:
            result1.append(now)
            visited[now] = 1
            for vertex in sorted(graph[now], reverse=True):
                if not visited[vertex]:
                    stack.append(vertex)


def bfs(start):
    que = [start]
    visited = [0] * (N + 1)
    while que:
        now = que.pop(0)
        if not visited[now]:
            result2.append(now)
            visited[now] = 1
            for vertex in sorted(graph[now]):
                if not visited[vertex]:
                    que.append(vertex)


N, M, V = map(int, input().split())
graph = {n: [] for n in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().split())
    if u in graph.keys():
        graph[u] += [v]
    else:
        graph[u] = [v]
    if v in graph.keys():
        graph[v] += [u]
    else:
        graph[v] = [u]

result1 = []
dfs(V)
print(*result1)

result2 = []
bfs(V)
print(*result2)
