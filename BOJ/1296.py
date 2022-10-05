import sys
input = lambda: sys.stdin.readline().rstrip()

YD = input()
N = int(input())

names = []
for _ in range(N):
    names.append(input())
names.sort()

max_odd = 0
max_idx = 0
for idx in range(N):
    L = YD.count('L') + names[idx].count('L')
    O = YD.count('O') + names[idx].count('O')
    V = YD.count('V') + names[idx].count('V')
    E = YD.count('E') + names[idx].count('E')
    odd = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    if max_odd < odd:
        max_odd = odd
        max_idx = idx

print(names[max_idx])
