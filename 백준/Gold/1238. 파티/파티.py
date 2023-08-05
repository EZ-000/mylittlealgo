import sys
import heapq
input = sys.stdin.readline


def dijkstra(start, end):
    global N
    inf = int(1e9)
    distance = [inf] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]


global N
N, M, X = map(int, input().split())
graph = [[] for i in range(N + 1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

max_time = 0
for n in range(1, N + 1):
    time = 0
    if n != X:
        time += dijkstra(n, X)
        time += dijkstra(X, n)
    if max_time < time:
        max_time = time

print(max_time)
