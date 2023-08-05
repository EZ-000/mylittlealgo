import sys
input = sys.stdin.readline

cnt = 0
while True:
    cnt += 1
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    else:
        ans = V // P * L
        mod = V % P
        ans += mod if mod < L else L
    print(f'Case {cnt}: {ans}')
