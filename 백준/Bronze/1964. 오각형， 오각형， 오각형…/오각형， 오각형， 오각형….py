N = int(input())
dots = 5
for n in range(2, N + 1):
    dots += 3 * n + 1
print(dots % 45678)
