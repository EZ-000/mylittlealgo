import sys
input = lambda: sys.stdin.readline().rstrip()


def blackjack(n, m, c):
    card3 = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                temp_sum = cards[i] + cards[j] + cards[k]
                if card3 < temp_sum <= m:
                    card3 = temp_sum
    return card3


N, M = map(int, input().split())
cards = sorted(list(map(int, input().split())), reverse=True)

print(blackjack(N, M, cards))
