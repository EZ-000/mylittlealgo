N = int(input())
arr = list(map(int, input().split()))

print(len(arr) - len(set(arr)))
