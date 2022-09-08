A = int(input())
B = int(input())

hun = B // 100
ten = (B - hun * 100) // 10
one = (B - hun * 100 - ten * 10)

print(A * one)
print(A * ten)
print(A * hun)
print(A * B)
