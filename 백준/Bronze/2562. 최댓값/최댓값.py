max_num = 0
max_idx = 0

for idx in range(9):
    num = int(input())
    if num > max_num:
        max_num = num
        max_idx = idx + 1

print(max_num)
print(max_idx)
