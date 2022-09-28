import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(list(set(nums)))
compress = {}

for idx, num in enumerate(sorted_nums):
    compress[num] = idx

for num in nums:
    print(compress[num], end=' ')
