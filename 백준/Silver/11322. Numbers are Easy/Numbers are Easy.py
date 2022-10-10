T = int(input())
for _ in range(T):
    N = int(input())
    for X in range(1, 10000000):
        binary = int(bin(X)[2:])
        if binary % N == 0:
            print(binary)
            break
