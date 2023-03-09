def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    delta = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for s in skill:
        type, r1, c1, r2, c2, degree = s
        if type == 1:
            delta[r1][c1] += -degree
            delta[r1][c2 + 1] += degree
            delta[r2 + 1][c1] += degree
            delta[r2 + 1][c2 + 1] += -degree
        elif type == 2:
            delta[r1][c1] += degree
            delta[r1][c2 + 1] += -degree
            delta[r2 + 1][c1] += -degree
            delta[r2 + 1][c2 + 1] += degree
    
    for r in range(N):
        for c in range(1, M):
            delta[r][c] += delta[r][c - 1]
    
    for c in range(M):
        for r in range(1, N):
            delta[r][c] += delta[r - 1][c]
            
    for r in range(N):
        for c in range(M):
            if 0 < board[r][c] + delta[r][c]:
                answer += 1
                
    return answer
