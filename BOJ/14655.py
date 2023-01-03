import sys
input = sys.stdin.readline

N = int(input())
R1 = list(map(int, input().split()))
R2 = list(map(int, input().split()))

R1 = [n if 0 < n else -n for n in R1]
R2 = [-n if 0 < n else n for n in R1]
print(sum(R1) - sum(R2))
