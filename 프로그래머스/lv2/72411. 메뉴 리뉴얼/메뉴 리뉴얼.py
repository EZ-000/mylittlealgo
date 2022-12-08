from itertools import combinations

def solution(orders, course):
    answer = []
    for num in course:
        choices = {}
        for order in orders:
            temp = combinations(sorted(list(order)), num)
            for comb in temp:
                if comb in choices.keys():
                    choices[comb] += 1
                else:
                    choices[comb] = 1
        max_cnt = max(choices.values(), default=0)
        if 1 < max_cnt:
            for key in choices:
                if choices[key] == max_cnt:
                    answer.append(''.join(key))
        answer.sort()
    return answer