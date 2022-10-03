# subset_recursion
import sys
input = sys.stdin.readline


def subset_recur(i, k):
    if i == k:
        temp = []
        for j in range(k):
            if bit[j]:
                temp += [seq[j]]
        subset.append(temp)
    else:
        bit[i] = 0
        subset_recur(i + 1, k)
        bit[i] = 1
        subset_recur(i + 1, k)


N, S = map(int, input().split())
seq = list(map(int, input().split()))
bit = [0] * N
subset = []

subset_recur(0, N)

cnt = 0
for s in subset:
    if s and sum(s) == S:
        cnt += 1
print(cnt)
