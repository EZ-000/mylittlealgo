N = int(input())
divisor = list(map(int, input().split()))
divisor.sort()

print(divisor[0] * divisor[-1])
