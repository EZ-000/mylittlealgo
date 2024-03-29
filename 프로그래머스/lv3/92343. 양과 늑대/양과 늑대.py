l = [-1] * 17
r = [-1] * 17
n = 0
val = []
answer = 1
vis = [0] * (1 << 17)


def sheep(s):
    global answer
    if vis[s]:
        return None
    vis[s] = 1
    wolf, vertex = 0, 0
    for i in range(n):
        if s & (1 << i):
            vertex += 1
            wolf += val[i]
    if vertex <= wolf * 2:
        return None
    answer = max(answer, vertex - wolf)

    for i in range(n):
        if s & (1 << i):
            if l[i] != -1:
                print(bin(s | (1 << l[i]))[2:])
                sheep(s | (1 << l[i]))
            if r[i] != -1:
                sheep(s | 1 << r[i])


def solution(info, edges):
    global n, val
    n = len(info)
    val = info[:]
    for u, v in edges:
        if l[u] == -1:
            l[u] = v
        else:
            r[u] = v
    sheep(1)
    return answer

# 참고: https://blog.encrypted.gg/1029
