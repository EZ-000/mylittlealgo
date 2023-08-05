import sys
input = sys.stdin.readline


N = int(input())
nums = []
for idx in range(N):
    nums.append(int(input()))
nums.sort()

ans = 0
for idx in range(1, N):
    nums[idx] += nums[idx - 1] + sum(nums[:idx])
print(nums[-1])
