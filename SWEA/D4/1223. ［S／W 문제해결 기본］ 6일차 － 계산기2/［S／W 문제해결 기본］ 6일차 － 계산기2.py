op = {'*': 2, '+': 1}

for t in range(1, 11):
    n = int(input())
    s = input()
    operators = []
    calculation = []

    for c in s:
        if c in op.keys():
            if not operators or op[operators[-1]] < op[c]:
                operators.append(c)
            else:
                while True:
                    if not operators or op[operators[-1]] < op[c]:
                        operators.append(c)
                        break
                    else:
                        if operators[-1] == '+':
                            temp = calculation[-1] + calculation[-2]
                        elif operators[-1] == '*':
                            temp = calculation[-1] * calculation[-2]
                        calculation.pop()
                        calculation.pop()
                        calculation.append(temp)
                        operators.pop()

        else:
            calculation.append(int(c))

    while operators:
        if operators[-1] == '+':
            temp = calculation[-1] + calculation[-2]
        elif operators[-1] == '*':
            temp = calculation[-1] * calculation[-2]
        calculation.pop()
        calculation.pop()
        calculation.append(temp)
        operators.pop()

    print(f'#{t} {calculation[0]}')
