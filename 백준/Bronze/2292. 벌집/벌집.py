N = int(input()) - 1
n = 1

while True:
    if N <= 0:
        print(n)
        break
    else:
        N -= 6 * n
        n += 1
