import sys
input = lambda: sys.stdin.readline().strip()

while True:
    s = input()
    if s == 'END':
        break
    else:
        print(s[::-1])
