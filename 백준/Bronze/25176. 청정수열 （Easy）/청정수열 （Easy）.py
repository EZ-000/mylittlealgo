import sys
input = sys.stdin.readline

N = int(input())
ans = 1
for n in range(2, N + 1):
    ans *= n

print(ans)
