import sys
input = sys.stdin.readline


N = int(input())
packs = [5, 3]
cnt = 0
for num in range(N // 5, -1, -1):
    if not (N - num * 5) % 3:
        print(num + (N - num * 5) // 3)
        break
else:
    print(-1)
