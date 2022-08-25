import sys
input = sys.stdin.readline

multi = 1
for _ in range(3):
    multi *= int(input())
multi = list(str(multi))

cnt = {}
for idx in range(10):
    cnt[idx] = multi.count(str(idx))

print(*cnt.values())
