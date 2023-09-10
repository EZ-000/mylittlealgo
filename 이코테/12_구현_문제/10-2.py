from copy import deepcopy


def rotate(arr):
    m = len(arr)
    rotated = [[0] * m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            rotated[r][c] = arr[m - c - 1][r]
    return rotated


def check(sr, sc, board, key, m, n):
    for r in range(m):
        for c in range(m):
            board[sr + r][sc + c] += key[r][c]

    for r in range(n):
        for c in range(n):
            if board[r + m - 1][c + m - 1] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)
    expanded_len = len(lock) + 2 * (len(key) - 1)
    expanded_lock = [[-1] * expanded_len for _ in range(expanded_len)]
    for r in range(n):
        for c in range(n):
            expanded_lock[r + m - 1][c + m - 1] = lock[r][c]

    for _ in range(4):
        key = rotate(key)
        for r in range(n + m - 1):
            for c in range(n + m - 1):
                board = deepcopy(expanded_lock)
                if check(r, c, board, key, m, n):
                    return True
    return False


k = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
l = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(k, l))

"""
테스트 1 〉	통과 (3.25ms, 10.3MB)
테스트 2 〉	통과 (0.14ms, 10.4MB)
테스트 3 〉	통과 (126.54ms, 10.3MB)
테스트 4 〉	통과 (1.08ms, 10.3MB)
테스트 5 〉	통과 (395.93ms, 10.2MB)
테스트 6 〉	통과 (375.08ms, 10.3MB)
테스트 7 〉	통과 (2412.86ms, 10.4MB)
테스트 8 〉	통과 (830.99ms, 10.3MB)
테스트 9 〉	통과 (1008.97ms, 10.5MB)
테스트 10 〉	통과 (2484.16ms, 10.5MB)
테스트 11 〉	통과 (4263.25ms, 10.3MB)
테스트 12 〉	통과 (0.10ms, 10.2MB)
테스트 13 〉	통과 (51.72ms, 10.4MB)
테스트 14 〉	통과 (7.20ms, 10.3MB)
테스트 15 〉	통과 (66.93ms, 10.4MB)
테스트 16 〉	통과 (770.97ms, 10.3MB)
테스트 17 〉	통과 (1202.24ms, 10.3MB)
테스트 18 〉	통과 (250.77ms, 10.4MB)
테스트 19 〉	통과 (4.31ms, 10.4MB)
테스트 20 〉	통과 (1156.96ms, 10.5MB)
테스트 21 〉	통과 (2602.30ms, 10.3MB)
테스트 22 〉	통과 (325.86ms, 10.3MB)
테스트 23 〉	통과 (38.86ms, 10.3MB)
테스트 24 〉	통과 (39.24ms, 10.3MB)
테스트 25 〉	통과 (2351.54ms, 10.3MB)
테스트 26 〉	통과 (3612.67ms, 10.3MB)
테스트 27 〉	통과 (7147.21ms, 10.4MB)
테스트 28 〉	통과 (443.68ms, 10.3MB)
테스트 29 〉	통과 (92.72ms, 10.3MB)
테스트 30 〉	통과 (561.88ms, 10.2MB)
테스트 31 〉	통과 (1310.75ms, 10.3MB)
테스트 32 〉	통과 (4126.21ms, 10.3MB)
테스트 33 〉	통과 (717.57ms, 10.2MB)
테스트 34 〉	통과 (30.44ms, 10.4MB)
테스트 35 〉	통과 (31.17ms, 10.2MB)
테스트 36 〉	통과 (51.29ms, 10.2MB)
테스트 37 〉	통과 (24.29ms, 10.3MB)
테스트 38 〉	통과 (4.69ms, 10.3MB)
"""