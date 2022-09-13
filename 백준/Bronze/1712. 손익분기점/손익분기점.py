A, B, C = map(int, input().split())
bep = int(A / (C - B)) + 1 if 0 < C - B else -1
print(bep)
