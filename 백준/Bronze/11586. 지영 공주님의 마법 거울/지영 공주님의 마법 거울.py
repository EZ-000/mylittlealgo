N = int(input())
image = []

for _ in range(N):
    image.append(input())

K = int(input())

if K == 1:
    print(*image, sep='\n')
elif K == 2:
    for i in range(N):
        image[i] = image[i][::-1]
    print(*image, sep='\n')
else:
    for i in range(N):
        print(image[N - i - 1])
