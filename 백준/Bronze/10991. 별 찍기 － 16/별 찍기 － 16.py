N = int(input())

for i in range(1, N + 1):
    print(' ' * (N - i), end='')
    for j in range(2 * i - 1):
        if j % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()
