N, M = map(int, input().split())
balls = list(map(int, input().split()))

weights = [0] * 11

for ball in balls:
    weights[ball] += 1

result = 0
for num in range(1, M + 1):
    N -= weights[num]
    result += weights[num] * N

print(result)
