from heapq import heappop, heappush


def solution(board):
    N = len(board)
    visited = [[[-1] * 4 for _ in range(N)] for _ in range(N)]
    heap = [(-1, 0, 0, 0)]  # direction, cost, x, y

    answer = -1
    while heap:
        d, c, x, y = heappop(heap)
        if x == y == N - 1 and (answer == -1 or c < answer):
            answer = c

        new_pos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for direction, (nx, ny) in enumerate(new_pos):
            if nx < 0 or ny < 0 or N - 1 < nx or N - 1 < ny:
                continue
            if board[nx][ny]:
                continue

            cost = c + (100 if d == direction or d == -1 else 600)
            if visited[nx][ny][direction] != -1 and visited[nx][ny][direction] < cost:
                continue

            heappush(heap, (direction, cost, nx, ny))
            visited[nx][ny][direction] = cost
    return answer
