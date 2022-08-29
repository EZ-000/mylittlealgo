def permutate(s, p):
    if s == M:
        print(*p)
        return

    for i in range(1, N + 1):
        if i not in p:
            p[s] = i
            permutate(s + 1, p)
            p[s] = 0


N, M = map(int, input().split())
P = [0] * M
permutate(0, P)
