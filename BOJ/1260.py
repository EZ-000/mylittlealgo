N, M, V = map(int, input().split())
graph = {}

for _ in range(M):
    u, v = map(int, input().split())
    if u in graph.keys():
        graph[u] += [v]
    else:
        graph[u] = [v]
    
# DFS
stack = [V]
visited = [0] * (N + 1)
dfs = []
while stack:
    if not visited[V]:
        dfs.append()