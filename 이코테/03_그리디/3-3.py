N, M = map(int, input().split())

cards = []
for _ in range(N):
    row = list(map(int, input().split()))
    row.sort()
    cards.append(row[0])

cards.sort()
print(cards[-1])
