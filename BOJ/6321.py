n = int(input())
for t in range(1, n + 1):
    s = input()
    com = ''
    for c in s:
        o = 65 if ord(c) == 90 else ord(c) + 1
        com += chr(o)
    print(f'String #{t}')
    print(com)
    print()
