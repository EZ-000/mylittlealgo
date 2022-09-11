def htod(h, d):
    l = len(h)
    for idx in range(l):
        if 47 < ord(hexa[idx]) < 58:
            d += int(hexa[idx]) * (16 ** (l - idx - 1))
        else:
            d += hdic[hexa[idx]] * (16 ** (l - idx - 1))
    return d


hexa = input()
hdic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

print(htod(hexa, 0))
