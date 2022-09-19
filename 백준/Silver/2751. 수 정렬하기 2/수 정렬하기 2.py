import sys
input = sys.stdin.readline

N = int(input())
ns = [0] * 2000001
for _ in range(N):
    ns[int(input()) + 1000000] += 1

for i in range(2000001):
    for j in range(ns[i]):
        print(i - 1000000)
