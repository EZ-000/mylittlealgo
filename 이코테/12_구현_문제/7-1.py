# 럭키 스트레이트
score = input()
mid = len(score) // 2

left = sum(map(int, list(score[:mid])))
right = sum(map(int, list(score[mid:])))

answer = "LUCKY" if left == right else "READY"
print(answer)
