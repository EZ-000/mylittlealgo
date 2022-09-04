N = int(input())

for i in range(1, 2 * N + 1):
    for j in range(1, N + 1):
        if i % 2:
            if j % 2:
                print('*', end='')
            else:
                print(' ', end='')
        else:
            if j % 2:
                print(' ', end='')
            else:
                print('*', end='')
    if i != 2 * N:
        print()
