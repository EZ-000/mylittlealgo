import sys
input = lambda: sys.stdin.readline().rstrip()

A = input()
B = input()
S = input()

answer = 'YES' if S in A and S in B else 'NO'
print(answer)
