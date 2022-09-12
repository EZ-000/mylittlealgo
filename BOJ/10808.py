s = input()
cnt = [0] * 26

for c in s:
    cnt[ord(c) - 97] += 1

print(*cnt)
