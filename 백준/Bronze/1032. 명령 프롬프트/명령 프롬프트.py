import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
files = []
for _ in range(N):
    files.append(input())

pattern = list(files[0])
for file in files[1:]:
    for idx in range(len(file)):
        if file[idx] != pattern[idx]:
            pattern[idx] = '?'

print(''.join(pattern))
