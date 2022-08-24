# PyPy3으로만 통과
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if N < M:
    N, M = M, N

for num in range(M, 0, -1):
    if N % num == 0 and M % num == 0:
        GCD = num
        break

num = N
for num in range(N, N * M + 1):
    if num % N == 0 and num % M == 0:
        LCM = num
        break

print(GCD)
print(LCM)
