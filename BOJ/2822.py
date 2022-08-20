s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())
s6 = int(input())
s7 = int(input())
s8 = int(input())

scores = [s1, s2, s3, s4, s5, s6, s7, s8]
sorted_s = sorted(scores, reverse=True)

top_5 = sorted_s[:5]
final_score = sum(top_5)
t = []
nth = []

for i, s in enumerate(scores):
    t.append((i, s))

for a in t:
    for ts in top_5:
        if a[1] == ts:
            nth.append(a[0] + 1)

print(final_score)

for i in nth:
    print(i, end=' ')