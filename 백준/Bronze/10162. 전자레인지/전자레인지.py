import sys
input = sys.stdin.readline

buttons = [300, 60, 10]

result = []
minutes = int(input())
for button in buttons:
    num = minutes // button
    result.append(num)
    minutes -= button * num

if minutes:
    print(-1)
else:
    print(*result)
