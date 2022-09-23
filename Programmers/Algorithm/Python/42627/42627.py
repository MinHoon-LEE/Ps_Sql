import heapq

## print 했을때 구조가 우리가 아는거랑은 다르게 보인다 ! 

def solution(jobs):
    hq = []
    current_time  = 0 
    jobs = sorted(jobs)
    length = len(jobs)
    count = 0
    i = 0
    time = 0
    while count != length:
        if i < length:
            while jobs[i][0] <= current_time:
                heapq.heappush(hq,(jobs[i][1],jobs[i]))
                i += 1
                if i >= length:
                    break
        if hq != []:
            tmp = heapq.heappop(hq)
            count += 1
            time += current_time - tmp[1][0] + tmp[1][1]
            current_time += tmp[1][1]
        else:
            current_time += 1
    return time // length
