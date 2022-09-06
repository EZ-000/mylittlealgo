from math import trunc


def sqr4(sqrt1):

    if N == sqrt1 ** 2:
        return 1

    while True:
        if sqrt1 == 0:
            break
        sqrt2 = trunc((N - sqrt1 ** 2) ** (1 / 2))
        if (N - sqrt1 ** 2) == sqrt2 ** 2:
            return 2
        sqrt1 -= 1

    n = 0
    while True:
        if N < 4 ** n:
            break
        if (N / (4 ** n) - 7) % 8 == 0:
            return 4
        n += 1

    return 3


N = int(input())
sqr = trunc(N ** (1 / 2))
print(sqr4(sqr))
