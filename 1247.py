import sys

for n in range(3):
    N = int(sys.stdin.readline())
    s = 0

    for nums in range(N):
        n = int(sys.stdin.readline())
        s += n

    if s == 0:
        print('0')
    elif s > 0:
        print('+')
    else:
        print('-')
