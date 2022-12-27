from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while True:
        min1 = heappop(scoville)
        if K <= min1:
            break
        if not scoville:
            answer = -1
            break
        else:
            answer += 1
            min2 = heappop(scoville)
            heappush(scoville, min1 + min2 * 2)
    return answer
