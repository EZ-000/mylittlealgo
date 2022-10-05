scores = []
accums = [0] * 10
diffes = [0] * 10

for _ in range(10):
    n = int(input())
    scores += [n]

accums[0] = scores[0]
for idx in range(1, 10):
    accums[idx] = accums[idx - 1] + scores[idx]

for idx in range(10):
    diffes[idx] = abs(100 - accums[idx])

mini = min(diffes)
if diffes.count(mini) == 2:
    print(100 + mini)
else:
    print(accums[diffes.index(mini)])
