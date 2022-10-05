import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
d = 0

for idx in range(1, n):
    d += arr[idx] - arr[idx - 1]
print(d)
