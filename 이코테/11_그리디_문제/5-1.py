N, M = map(int, input().split())
balls = list(map(int, input().split()))

offset = len(balls) - len(set(balls))
print((N * (N - 1)) // 2 - offset)
