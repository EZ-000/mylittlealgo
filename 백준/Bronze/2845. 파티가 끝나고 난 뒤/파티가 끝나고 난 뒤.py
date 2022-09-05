L, P = map(int, input().split())
numbers = list(map(int, input().split()))
real_num = L * P

for num in numbers:
    print(num - real_num, end=' ')
