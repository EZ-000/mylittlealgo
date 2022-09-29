import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    s = list(input().split(' '))
    for w in s:
        print(w[::-1], end=' ')
