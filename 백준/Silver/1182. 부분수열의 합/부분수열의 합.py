N, S = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0
for i in range(1 << N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append(seq[j])
    if subset and sum(subset) == S:
        cnt += 1
print(cnt)
