import sys
input = sys.stdin.readline


N = int(input())
peaks = list(map(int, input().split()))
kills = [0] * N

top = peaks[0]
for idx in range(N - 1):
    if peaks[idx + 1] < top:
        kills[idx + 1] = kills[idx] + 1
    else:
        top = peaks[idx + 1]
        kills[idx + 1] = 0

print(max(kills))
