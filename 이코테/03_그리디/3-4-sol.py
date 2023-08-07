N, K = map(int, input().split())
answer = 0

while True:
    target = (N // K) * K
    answer += (N - target)
    N = target

    if N < K:
        break

    answer += 1
    N //= K

answer += (N - 1)
print(answer)
