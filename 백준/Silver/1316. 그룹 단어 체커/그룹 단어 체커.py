import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    s = input()
    check = []
    for i in range(len(s)):
        if s[i] not in check:
            check.append(s[i])
        elif s[i] in check and s[i] != s[i - 1]:
            break
    else:
        cnt += 1

print(cnt)
