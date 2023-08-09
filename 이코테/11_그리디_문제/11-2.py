# 곱하기 혹은 더하기
numbers = input()

answer = int(numbers[0])
for index in range(len(numbers) - 1):
    now = int(numbers[index])
    number = int(numbers[index + 1])
    if now == 0 or now == 1:
        answer += number
    else:
        answer *= number

print(answer)
