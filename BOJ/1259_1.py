import sys

while True:
    i = sys.stdin.readline().rstrip()
    if i == '0':
        break
    else:
        if i == i[::-1]:
            print('yes')
        else:
            print('no')
