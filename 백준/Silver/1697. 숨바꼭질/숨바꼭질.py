from collections import deque


def hide_n_seek(n, k):
    node = deque([n])
    visited = [0] * 100001
    while node:
        now = node.popleft()
        if now == k:
            return visited[now]
        else:
            for new in [now - 1, now + 1, 2 * now]:
                if 0 <= new <= 100000 and not visited[new]:
                    node.append(new)
                    visited[new] = visited[now] + 1


N, K = map(int, input().split())
print(hide_n_seek(N, K))
