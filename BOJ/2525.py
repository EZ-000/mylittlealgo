A, B = map(int, input().split())
C = int(input())

h = A + (B + C) // 60
m = (B + C) % 60

h = h if h < 24 else h - 24

print(h, m)
