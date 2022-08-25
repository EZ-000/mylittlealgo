N1, N2 = input().split()

N1 = int(N1[::-1])
N2 = int(N2[::-1])

print(N1) if N1 > N2 else print(N2)
