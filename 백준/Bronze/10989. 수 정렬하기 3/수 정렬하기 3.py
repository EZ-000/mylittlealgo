import sys
input = sys.stdin.readline

N = int(input())
ns = [0] * 10001
for _ in range(N):
    ns[int(input())] += 1

for i in range(1, 10001):
    for j in range(ns[i]):
        print(i)
