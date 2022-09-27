T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    cnt = 0
    for n in range(N, M + 1):
        cnt += str(n).count('0')
    print(cnt)
