T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])
