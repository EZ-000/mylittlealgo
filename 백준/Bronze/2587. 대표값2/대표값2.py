import sys
input = sys.stdin.readline

nums = []
total = 0

for _ in range(5):
    n = int(input())
    total += n
    nums += [n]

print(total // 5)

nums.sort()
print(nums[2])
