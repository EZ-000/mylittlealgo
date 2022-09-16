T = int(input())

for t in range(1, T + 1):
    n = int(input())
    sqrt = round(n ** (1 / 3))
    if sqrt ** 3 != n:
        sqrt = -1
    print(f'#{t} {sqrt}')
