from itertools import combinations
import sys

heights = []
for n in range(9):
    height = int(sys.stdin.readline())
    heights.append(height)
heights.sort()

combi = list(combinations(heights, 7))

for c in combi:
    if sum(c) == 100:
        for n in c:
            print(n)
        break
