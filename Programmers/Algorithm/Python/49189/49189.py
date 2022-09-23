from collections import deque

def solution(n, vertex):
    que = deque()
    que.append(1)
    dic = [0] * (n+1)
    graph = [[] for i in range(n+1)]
    for x,y in vertex:
        graph[x].append(y)
        graph[y].append(x)
    dic[1] = 1 
    while que:
        node = que.popleft()
        for j in graph[node]:
            if dic[j] == 0:
                dic[j] = dic[node] + 1
                que.append(j)
    count = 0
    maximum = max(dic)
    for i in dic:
        if i == maximum:
            count += 1
    return count
