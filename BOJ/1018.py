N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

chess1 = []
chess2 = []
for idx in range(8):
    if idx % 2:
        chess1.append('WBWBWBWB')
        chess2.append('BWBWBWBW')
    else:
        chess1.append('BWBWBWBW')
        chess2.append('WBWBWBWB')


def recoloring(n, m, arr):
    recolor1 = 65
    recolor2 = 65
    for i in range(n - 8 + 1):
        for j in range(m - 8 + 1):
            temp1 = 0
            temp2 = 0
            for w1 in range(8):
                for w2 in range(8):
                    if arr[i + w1][j + w2] != chess1[w1][w2]:
                        temp1 += 1
                    if arr[i + w1][j + w2] != chess2[w1][w2]:
                        temp2 += 1
            if temp1 < recolor1:
                recolor1 = temp1
            if temp2 < recolor2:
                recolor2 = temp2
    return min(recolor1, recolor2)


print(recoloring(N, M, board))

''' 수업시간에 배웠던 방법대로 4중 for문으로 풀었다.
더 깔끔한 코드가 있을 것 같다!
'''
