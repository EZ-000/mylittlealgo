N = int(input())

for n in range(1, N + 1):
    blank = (2 * N - 2 * n) // 2
    print(' ' * blank + '*' * (2 * n - 1))
