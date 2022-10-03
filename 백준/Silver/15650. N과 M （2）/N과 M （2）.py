import sys
input = sys.stdin.readline


def ncr(n, r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n - r + 1):
            comb[M - r] = seq[i]
            ncr(n, r - 1, i + 1)


N, M = map(int, input().split())
seq = [n for n in range(1, N + 1)]
comb = [0] * M

ncr(N, M, 0)
