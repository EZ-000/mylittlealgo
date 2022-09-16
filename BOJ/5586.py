s = input()
l = len(s)
joi = 0
ioi = 0

while s:
    if s[0:3] == 'JOI':
        joi += 1
        s = s[2:]
    elif s[0:3] == 'IOI':
        ioi += 1
        s = s[2:]
    else:
        s = s[1:]

print(joi)
print(ioi)
