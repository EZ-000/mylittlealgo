import sys
input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))
ropes.sort()

maxi = 0
for i in range(N):
    temp = ropes[i] * (N - i)
    if maxi < temp:
        maxi = temp
print(maxi)
