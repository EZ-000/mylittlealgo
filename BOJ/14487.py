import sys
input = sys.stdin.readline


n = int(input())
cost = list(map(int, input().split()))
print(sum(cost) - max(cost))
