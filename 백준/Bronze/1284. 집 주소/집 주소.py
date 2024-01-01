while True:
    address = input()
    if address == '0':
        break
    else:
        answer = len(address) + 1
        for c in address:
            if c == '1':
                answer += 2
            elif c == '0':
                answer += 4
            else:
                answer += 3
        print(answer)