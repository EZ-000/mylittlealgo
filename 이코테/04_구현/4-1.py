# 왕실의 나이트
start = input()
r = int(start[1])
c = ord(start[0]) - ord('a') + 1

count = 0
directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
for direction in directions:
    nr = r + direction[0]
    nc = c + direction[1]
    if 0 < nr < 9 and 0 < nc < 9:
        count += 1

print(count)
