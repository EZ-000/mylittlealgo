def reversed_bin(num):
    B = ''
    i = 0
    while True:
        if num - 2 ** i < 0:
            break
        if num & (1 << i):
            B += '1'
        else:
            B += '0'
        i += 1
    return B


T = int(input())
for _ in range(T):
    n = int(input())
    binary = reversed_bin(n)
    for idx in range(len(binary)):
        if binary[idx] == '1':
            print(idx, end=' ')
