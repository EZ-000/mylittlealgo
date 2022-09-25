A, B = map(int, input().split())
seq = []

n = 0
while True:
    if B < len(seq):
        break
    n += 1
    seq += [n] * n

print(sum(seq[A - 1:B]))
