import sys
input = lambda: sys.stdin.readline().rstrip()

A = input()
B = input()
S = input()
s = ''
temp_s = ''

for idx in len(B):
    if c1 == c2:
        temp_s += c1
    else:
        if len(s) < len(temp_s):
            s = temp_s
            temp_s = ''
print(s)

answer = ''
answer = 'YES' if s == S else 'NO'
print(answer)
