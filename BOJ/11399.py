import sys
input = sys.stdin.readline

N = int(input())
minutes = sorted(list(map(int, input().split())))

accum = 0
for idx in range(N):
    accum += minutes[idx]
    minutes[idx] = accum
print(sum(minutes))
