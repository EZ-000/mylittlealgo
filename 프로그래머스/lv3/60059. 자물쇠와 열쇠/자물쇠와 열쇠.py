from copy import deepcopy


def rotate(pre_key):                                        # 시계방향으로 90도 회전하는 함수
    L = len(pre_key)
    rot_key = [[] for _ in range(L)]
    for i in range(L):
        for j in range(L):
            rot_key[i].append(pre_key[L - j - 1][i])
    return rot_key


def check(row, col, now_key, lock_copy):                    # params: 현재 시작 위치, 현재 열쇠의 모양, 확장된 자물쇠의 복사본
    for i in range(M):                                      # return: boolean 자물쇠가 열리는지 여부             
        for j in range(M):
            lock_copy[i + row][j + col] += now_key[i][j]

    cnt = 0
    for i in range(N):
        for j in range(N):
            now = lock_copy[M - 1 + i][M - 1 + j]
            if now != 1:                                    # 모두 1인 경우만 True
                return False
    return True
    
    
def solution(key, lock):
    global N
    global M
    global L

    N = len(lock)
    M = len(key)
    
    add_in = [1] * (M - 1)                                      # 자물쇠 확장
    add_out = [1] * (2 * M + N - 2)
    exp_lock = [add_out] * (M - 1) + [add_in + l + add_in for l in lock] + [add_out] * (M - 1)
    L = len(exp_lock)
    
    for _ in range(4):                                          # 360도 돌면서 확인
        key = rotate(key)
        for i in range(N + M - 1):
            for j in range(N + M - 1):
                lcopy = deepcopy(exp_lock)
                if check(i, j, key, lcopy):
                    return True           
    return False
