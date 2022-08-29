N = int(input())

for num in range(N // 2, N):
    lst_num = list(str(num))
    disassum = 0

    for n in lst_num:
        disassum += int(n)
    disassum += num

    if disassum == N:
        print(num)
        break

else:
    print(0)
