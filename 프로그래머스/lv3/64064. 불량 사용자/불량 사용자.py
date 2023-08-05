import re
from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    r = len(banned_id)
    perms = list(map(list, permutations(user_id, r)))
    banned_id = [re.sub('\*', '.', id) for id in banned_id]
                 
    for perm in perms:
        for i in range(r):
            temp = re.match('^' + banned_id[i] + '$', perm[i])
            if not temp:
                break
        else:
            perm.sort()
            if perm not in answer:
                answer.append(perm)
                
    return len(answer)
