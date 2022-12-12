import sys
input = sys.stdin.readline


N = int(input())
stores = map(int, input().split())
cnt = 0
kind = 0
for store in stores:    
    if store == kind:
        cnt += 1
        kind += 1
        if kind == 3:
            kind = 0
print(cnt)
