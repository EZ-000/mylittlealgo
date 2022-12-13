import sys
input = sys.stdin.readline


def five_six(arr):
    temp5 = ''
    temp6 = ''
    for n in arr:
        if n == '5' or n == '6':
            temp5 += '5'
            temp6 += '6'
        else:
            temp5 += n
            temp6 += n
    return [int(temp5), int(temp6)]


A, B = map(list, input().split())
A5, A6 = five_six(A)
B5, B6 = five_six(B)

print(A5 + B5, A6 + B6)
