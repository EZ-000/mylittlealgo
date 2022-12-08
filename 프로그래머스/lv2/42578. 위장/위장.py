def solution(clothes):

    from collections import Counter
    answer = 1

    clothes = dict(clothes)
    v = clothes.values()
    c = Counter(v)

    for i in c:
        answer *= c[i] + 1
    answer = answer - 1

    return answer