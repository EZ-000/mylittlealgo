import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

max_num = -1000001
min_num = 1000001

for num in nums:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(min_num, max_num)
