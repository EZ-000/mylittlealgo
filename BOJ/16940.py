def bfs(start):
    result = [1]
    while que:
        print('que', que)
        now = que.pop(0)
        if not visited[now]:
            result.append(now)
            visited[now] = 1
            print('visited', visited)
            print('result', result)
            for vertex in tree[now]:
                if not visited[vertex]:
                    que.append(vertex)

    return result


N = int(input())
tree = {n: [] for n in range(N + 1)}
for _ in range(N - 1):
    u, v = map(int, input().split())
    if u in tree.keys():
        tree[u] += [v]
    else:
        tree[u] = [v]
    if v in tree.keys():
        tree[v] += [u]
    else:
        tree[v] = [u]
submission = list(map(int, input().split()))

answers = []
for n in tree[1]:
    visited = [0] * (N + 1)
    visited[1] = 1
    que = [n]
    answers.append(bfs(n))

print(answers)
