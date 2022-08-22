import sys

while True:
    i = sys.stdin.readline().rstrip()
    if i == '0':
        break
    else:
        cnt = 0
        for j in range(len(i) // 2):
            if i[j] == i[-j - 1]:
                cnt += 1
        if cnt == len(i) // 2:
            print('yes')
        else:
            print('no')
