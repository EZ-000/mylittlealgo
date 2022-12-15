import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    prizes = []
    for _ in range(n):
        prizes.append(list(map(int, input().split())))
    prizes.sort(key=lambda x: -x[-1])

    stickers = list(map(int, input().split()))
    money = 0
    for prize in prizes:
        flag = 0
        while True:
            if flag == 1:
                break
            temp = stickers[:]
            for n in prize[1:-1]:
                if stickers[n - 1] == 0:
                    stickers = temp[:]
                    flag = 1
                    break
                else:
                    stickers[n - 1] -= 1
            else:
                money += prize[-1]
    print(money)
