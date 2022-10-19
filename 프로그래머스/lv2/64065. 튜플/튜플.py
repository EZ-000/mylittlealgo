def solution(s):
    answer = []
    sets = []
    flag = 0
    num = ''
    for c in s[1:-1]:
        if c == '{':
            temp = []
            flag = 1
        elif c == '}':
            temp.append(int(num))
            num = ''
            sets.append(temp)
            flag = 0
        elif c == ',':
            if flag:
                temp.append(int(num))
                num = ''
        else:
            num += c
    
    sets.sort(key = lambda x: len(x))
    
    for elem in sets:
        for n in elem:
            if n not in answer:
                answer.append(n)
                
    return answer