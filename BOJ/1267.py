N = int(input())
Y = 0
M = 0
T = list(map(int, input().split()))
for t in T:
    Y += 10 * (t // 30 + 1)
    M += 15 * (t // 60 + 1)

if Y < M:
    print('Y', Y)
elif M < Y:
    print('M', M)
else:
    print('Y', 'M', Y)
