N, B = input().split()

L = len(N)
B = int(B)
deci = 0

for i in range(L):
    if 47 < ord(N[L - i - 1]) < 58:
        deci += int(N[L - i - 1]) * (B ** i)
    else:
        deci += (ord(N[L - i - 1]) - 55) * (B ** i)

print(deci)
