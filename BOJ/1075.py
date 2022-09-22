N = int(input())
F = int(input())

for idx in range(99):
    if idx < 10:
        lasttwo = '0' + str(idx)
        n = int(str(N)[:-2] + lasttwo)
    else:
        lasttwo = str(idx)
        n = int(str(N)[:-2] + lasttwo)
    
    if n % F == 0:
        print(lasttwo)
        break
