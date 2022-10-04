import heapq

def solution(operations):
    answer = []
    
    heap = []
    len = 0
    for i in operations:
        tmp = i.split()
        if tmp[0] == "I":
            heapq.heappush(heap,int(tmp[1]))
            len += 1
        else:
            if not len == 0:
                if tmp[1] == "-1":
                    heapq.heappop(heap)
                elif tmp[1] == "1":
                    heap.sort()
                    heap = heap[:len-1]
                len -= 1
    if heap == []:
        return [0,0]
    heap.sort()
    answer = [heap[len-1],heap[0]]
    return answer
