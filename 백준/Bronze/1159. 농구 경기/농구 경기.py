N = int(input())
cnt = {}
for _ in range(N):
    surname = input()
    if surname[0] in cnt.keys():
        cnt[surname[0]] += 1
    else:
        cnt[surname[0]] = 1

chars = []
for char, num in cnt.items():
    if 4 < num:
        chars += [char]

chars.sort()
if chars == []:
    print('PREDAJA')
else:
    print(''.join(chars))
