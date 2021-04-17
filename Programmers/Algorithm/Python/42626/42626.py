import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K and len(scoville) > 1:
        tmp = heapq.heappop(scoville) +  heapq.heappop(scoville) * 2
        heapq.heappush(scoville,tmp)
        answer += 1
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    return answer
