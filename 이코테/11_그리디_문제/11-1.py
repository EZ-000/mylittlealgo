# 모험가 길드
# 내림차순 틀린 풀이
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
index = len(arr)
while True:
    count = arr[index - 1]
    index -= count
    if index < 0:
        break
    answer += 1

print(answer)
