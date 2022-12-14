import sys
input = lambda: sys.stdin.readline().rstrip()


N = int(input())
seats = list(input())
holders = [1] * (N + 1)
flag = 0
for idx in range(1, N):
    if seats[idx] == 'L':
        if not flag:
            holders[idx] = 0
            flag = 1
        else:
            flag = 0

temp = sum(holders)
ans = temp if temp < N else N
print(ans)
