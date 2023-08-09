S = input()

flag = S[0]
zero = 1 if flag == "0" else 0
one = 1 if flag == "1" else 0
for n in S:
    if n != flag:
        if n == "0":
            zero += 1
        else:
            one += 1

answer = zero if zero < one else one
print(answer)
