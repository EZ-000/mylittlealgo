import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().split())
fatigue = 0
work = 0
for _ in range(24):
    if M < A:
        break
    if fatigue + A <= M:
        fatigue += A
        work += B
    else:
        fatigue -= C
        if fatigue < 0:
            fatigue = 0
print(work)
