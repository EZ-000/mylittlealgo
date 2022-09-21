N, K = map(int, input().split())

cnt = 0
for divisor in range(1, N + 1):
    if N % divisor == 0:
        cnt += 1
        if cnt == K:
            print(divisor)
            break
else:
    print(0)
