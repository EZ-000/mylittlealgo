import sys
input = lambda: sys.stdin.readline().rstrip()

scale = ''.join(input().split())

asc = '12345678'
dsc = '87654321'

if scale == asc:
    print('ascending')
elif scale == dsc:
    print('descending')
else:
    print('mixed')
