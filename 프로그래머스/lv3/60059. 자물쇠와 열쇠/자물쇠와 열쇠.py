from copy import deepcopy


def rotate(pre_key):
    L = len(pre_key)
    rot_key = [[] for _ in range(L)]
    for i in range(L):
        for j in range(L):
            rot_key[i].append(pre_key[L - j - 1][i])
    return rot_key


def check(row, col, now_key, lock_copy):
    for i in range(M):
        for j in range(M):
            lock_copy[i + row][j + col] += now_key[i][j]

    cnt = 0
    for i in range(N):
        for j in range(N):
            now = lock_copy[M - 1 + i][M - 1 + j]
            if now != 1:
                return False
    return True
    
    
def solution(key, lock):
    global N
    global M 
    global L
    
    N = len(lock)
    M = len(key)
    add = [1] * (M - 1)
    exp_lock = [add + l + add for l in lock]
    
    add_lst = [1] * (2 * M + N - 2)
    exp_lock = [add_lst] * (M - 1) + exp_lock + [add_lst] * (M - 1)
    L = len(exp_lock)
    
    answer = True
    for _ in range(4):
        key = rotate(key)
        for i in range(N + M - 1):
            for j in range(N + M - 1):
                lcopy = deepcopy(exp_lock)
                if check(i, j, key, lcopy):
                    return answer
    answer = False            
    return answer
