# 모험가 길드
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
count = 0
for n in arr:
    count += 1
    if n <= count:
        answer += 1
        count = 0

print(answer)
