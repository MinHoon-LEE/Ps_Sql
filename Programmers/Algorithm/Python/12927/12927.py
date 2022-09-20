import heapq

def solution(n, works):
    answer = 0
    works = sorted(works)
    hq = []
    for i in range(len(works)):
        heapq.heappush(hq,-works[i])
    for i in range(n):
        tmp = heapq.heappop(hq)
        if tmp < 0:
            heapq.heappush(hq,tmp+1)
        else:
            heapq.heappush(hq,tmp)
            break
        
    for i in range(len(works)):
        answer += heapq.heappop(hq) ** 2 
    return answer
