import sys
input = lambda: sys.stdin.readline().rstrip()

S = input()
K = input()
s = ''

for c in S:
    if not 47 < ord(c) < 58:
        s += c

answer = int()
answer = 1 if K in s else 0
print(answer)
