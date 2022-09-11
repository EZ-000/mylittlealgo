A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = A * P
if C < P:
    Y = B + D * (P - C)
else:
    Y = B

rate = X if X < Y else Y

print(rate)
