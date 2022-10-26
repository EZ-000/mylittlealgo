def solution(str1, str2):
    str1 = list(str1.upper())
    str2 = list(str2.upper())
    
    temp1 = []
    temp2 = []
    for i in range(len(str1) - 1):
        temp1.append(str1[i] + str1[i + 1])
    for i in range(len(str2) - 1):
        temp2.append(str2[i] + str2[i + 1])
    
    set1 = []
    set2 = []
    for cs in temp1:
        for c in cs:
            if ord(c) not in range(65, 91):
                break
        else:
            set1.append(cs)
    for cs in temp2:
        for c in cs:
            if ord(c) not in range(65, 91):
                break
        else:
            set2.append(cs)

    if len(set2) < len(set1):
        set1, set2 = set2, set1

    L1 = len(set1)
    L2 = len(set2)
    inter = []
    visited = [0] * L2
    for i in range(L1):
        for j in range(L2):
            if set1[i] == set2[j] and not visited[j]:
                inter.append(set1[i])
                visited[j] = 1
                break
    print(inter)
    LI = len(inter)
    if L1 == L2 == 0:
        answer = 65536
    else:
        answer = int((LI / (L1 + L2 - LI)) * 65536)
    return answer
