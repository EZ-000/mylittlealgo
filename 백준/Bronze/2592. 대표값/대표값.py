import sys
input = sys.stdin.readline

frequency = {}
total = 0

for _ in range(10):
    n = int(input())
    total += n
    if n in frequency.keys():
        frequency[n] += 1
    else:
        frequency[n] = 1

print(total // 10)

f = sorted(frequency, key=lambda x: frequency[x])
print(f[-1])
