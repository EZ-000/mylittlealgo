import sys
input = sys.stdin.readline

cnt = 0
while True:
    kangaroos = list(map(int, input().split()))
    if not kangaroos:
        break
    else:
        A, B, C = kangaroos
        while True:
            left = B - A
            right = C - B
            if left == right == 1:
                print(cnt)
                cnt = 0
                break
            else:
                cnt += 1
                if left < right:
                    A, B, C = B, B + 1, C
                else:
                    A, B, C = A, A + 1, B
