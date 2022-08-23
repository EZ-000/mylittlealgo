import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    temp = 0
    score = 0
    for ox in input():
        if ox == 'O':
            temp += 1
            score += temp
        else:
            temp = 0
    print(score)
