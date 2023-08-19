# 1로 만들기
import time
start = time.time()

X = int(input())
d = {X: 0}

r = 0
keys = [X]
while 1 not in d:
    r += 1
    new_keys = []
    for k in keys:
        if not k % 5:
            d[k // 5] = r
            new_keys.append(k // 5)
        if not k % 3:
            d[k // 3] = r
            new_keys.append(k // 3)
        if not k % 2:
            d[k // 2] = r
            new_keys.append(k // 2)
        d[k - 1] = r
        new_keys.append(k - 1)
    keys = new_keys[:]

print(r)
print(time.time() - start)
