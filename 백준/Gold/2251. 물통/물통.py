volumes = list(map(int, input().split()))

now = (0, 0, volumes[2])
que = [now]
pre_dir = {now: (-1, -1)}
answer = set()
visited = {now}

while que:
    now = que.pop(0)
    if not now[0]:
        answer.add(now[2])
    for s in range(3):
        for e in range(3):
            if s != e and now[s] and not (s in pre_dir[now] and e in pre_dir[now]):
                new = list(now[:])
                temp = now[s] + now[e]
                if volumes[e] < temp:
                    new[s] = temp - volumes[e]
                    new[e] = volumes[e]
                else:
                    new[s] = 0
                    new[e] = temp
                new = tuple(new)
                if new not in visited:
                    que.append(new)
                    visited.add(new)
                pre_dir[new] = (s, e)

print(*sorted(list(answer)))
