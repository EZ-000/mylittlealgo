import sys

N = int(sys.stdin.readline())
words = list(set([sys.stdin.readline().rstrip() for _ in range(N)]))

words.sort()
words.sort(key=lambda word: len(word))

for word in words:
    print(word)
