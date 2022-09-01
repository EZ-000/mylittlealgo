N = int(input())

for n in range(1, N + 1):
    blank = (2 * N - 2 * n) // 2
    print(' ' * blank + '*' * (2 * n - 1))

for n in range(N - 1, 0, -1):
    blank = (2 * N - 2 * n) // 2
    print(' ' * blank + '*' * (2 * n - 1))
