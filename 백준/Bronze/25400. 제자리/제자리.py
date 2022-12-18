import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
num = 1
for card in cards:
    if card == num:
        num += 1

print(N - num + 1)
