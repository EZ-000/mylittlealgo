def solution(s):
    shortest = len(s)
    for length in range(1, len(s) // 2 + 1):
        zipped = ""
        rep = 1
        for index in range(0, len(s), length):
            pre = s[index:index + length]
            post = s[index + length:index + length * 2]
            if pre == post:
                rep += 1
            else:
                zipped += pre if rep == 1 else str(rep) + pre
                rep = 1

        if len(zipped) < shortest:
            shortest = len(zipped)

    return shortest
