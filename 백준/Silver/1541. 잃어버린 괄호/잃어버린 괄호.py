import sys
input = lambda: sys.stdin.readline().rstrip()

E = input() + '+'
plus = 0
minus = 0
flag = 1
temp = ''
for c in E:
    if c == '+':
        if flag:
            plus += int(temp)
        else:
            minus += int(temp)
        temp = ''
    elif c == '-':
        if flag:
            flag = 0
            plus += int(temp)
        else:
            minus += int(temp)
        temp = ''
    else:
        temp += c
print(plus - minus)
