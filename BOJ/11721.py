s = input()
while True:
    if not s:
        break
    print(s[:10])
    s = s[10:]
