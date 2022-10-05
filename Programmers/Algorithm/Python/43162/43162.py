from collections import deque

def solution(n, computers):
    answer = 0
    found = [0] * n
    graph = [[] for i in range (n)]
    for i in range (n):
        for j in range (n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
    for i in range (n):
        if found[i] == 0:
            answer += 1
            dq = deque()
            dq.append(i)
            while dq:
                tmp = dq.popleft()
                if found[tmp] == 0:
                    found[tmp] = 1
                    for x in graph[tmp]:
                        if found[x] == 0:
                            dq.append(x)      
    return answer
