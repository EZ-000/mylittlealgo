X, Y = input().split()
X = int(X[::-1])
Y = int(Y[::-1])

rev = int(str(X + Y)[::-1])
print(rev)
