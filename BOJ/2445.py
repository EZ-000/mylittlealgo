N = int(input())

for n in range(1, N + 1):
    blank = 2 * N - 2 * n
    print('*' * n + ' ' * blank + '*' * n)

for n in range(N - 1, 0, -1):
    blank = 2 * N - 2 * n
    print('*' * n + ' ' * blank + '*' * n)
