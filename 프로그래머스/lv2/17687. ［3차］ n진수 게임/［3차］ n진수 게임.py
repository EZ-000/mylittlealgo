def base(num, q):
    rev_base = ''

    while num > 0:
        num, mod = divmod(num, q)
        if 9 < mod:
            rev_base += chr(mod + 55)
        else:
            rev_base += str(mod)

    return rev_base[::-1]
# 참고: https://velog.io/@code_angler/파이썬-진수변환2진법-3진법-5진법-10진법n진법

def solution(n, t, m, p):
    answer = ''
    total = '0'
    cnt = 1
    while len(total) < t * m:
        temp = base(cnt, n)
        total += temp
        cnt += 1
    for i in range(t):
        answer += total[m * i + (p - 1)]

    return answer
