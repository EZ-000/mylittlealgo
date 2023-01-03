import sys
input = lambda: sys.stdin.readline().rstrip()

S = list(input())
L = len(S)

cnt = 1
for idx in range(L - 1):
    if ord(S[idx + 1]) <= ord(S[idx]):
        cnt += 1
print(cnt)
