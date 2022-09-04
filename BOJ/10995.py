N = int(input())

for i in range(1, N + 1):
    if i % 2:
        for j in range(2 * N - 1):
            if j % 2:
                print(' ', end='')
            else:
                print('*', end='')
    else:
        for j in range(2 * N):
            if j % 2:
                print('*', end='')
            else:
                print(' ', end='')
    print()
