import sys
input = sys.stdin.readline


N = int(input())
result = '12' * (N // 2)
if N % 2:
    result += '3'
print(*list(result))
