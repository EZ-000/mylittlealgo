import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    R, S = input().split()
    result = ''
    for c in S:
        result += c * int(R)
    print(result)
