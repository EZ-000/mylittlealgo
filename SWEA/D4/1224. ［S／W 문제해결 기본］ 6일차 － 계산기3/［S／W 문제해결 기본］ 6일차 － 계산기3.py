icp = {'(': 3, '*': 2, '+': 1}
isp = {'(': 0, '*': 2, '+': 1}

for t in range(1, 11):
    n = int(input())
    s = input()
    operators = []
    calculation = []

    for c in s:
        if c in icp.keys():
            if not operators or isp[operators[-1]] < icp[c]:
                operators.append(c)
            else:
                while True:
                    if not operators or isp[operators[-1]] < icp[c]:
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

        elif c == ')':
            while True:
                if operators[-1] == '(':
                    operators.pop()
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

    print(f'#{t} {calculation[0]}')
