# 문자열 재정렬
s = sorted(list(input()))

answer = ""
num = 0
for c in s:
    if ord("A") <= ord(c) <= ord("Z"):
        answer += c
    else:
        num += int(c)

answer += str(num)
print(answer)
