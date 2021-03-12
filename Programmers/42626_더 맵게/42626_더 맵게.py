import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) > 1:
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            new = min1 + min2*2
            heapq.heappush(scoville, new)
            answer += 1
        else:
            return -1
    return answer