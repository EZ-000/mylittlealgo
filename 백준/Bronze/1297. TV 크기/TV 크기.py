d, H, W = map(int, input().split())

D = (W ** 2 + H ** 2) ** 0.5
h = H * d / D
w = W * d / D

print(int(h), int(w))
