A, B = map(int, input().split())
if B < A:
    A, B = B, A
p = A + B
m = B - A

if m % 2:
    print(p * ((m + 1) // 2))
else:
    print(p * (m // 2) + (p // 2))
