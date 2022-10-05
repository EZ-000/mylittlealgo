import sys
input = sys.stdin.readline


def ncr(n, r, s):
    if r == 0:
        combs.append(comb[:])
    else:
        for i in range(s, n - r + 1):
            comb[3 - r] = nums[i]
            ncr(n, r - 1, i + 1)


nums = list(map(int, input().split()))
nums.sort()
combs = []
comb = [0] * 3
ncr(5, 3, 0)

answer = 0
for multi in range(nums[0], nums[0] * nums[1] * nums[2] + 1):
    for comb in combs:
        if multi % comb[0] == 0 and multi % comb[1] == 0 and multi % comb[2] == 0:
            answer = multi
            break
    if answer:
        break
print(answer)
