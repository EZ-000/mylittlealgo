N = input()
new = list(N)
S = int()
times = 0

while True:
    times += 1
    if len(new) == 1:
        new.insert(0, '0')

    S = int(new[0]) + int(new[1])
    zero = new[-1]
    one = list(str(S))[-1]
    new = [zero, one]

    if int(N) == int(new[0] + new[1]):
        break

print(times)