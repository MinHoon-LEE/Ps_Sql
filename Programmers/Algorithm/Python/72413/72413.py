from collections import deque 

def solution(n, s, a, b, fares):
    answer = int(1e9)
    INF = int(1e9)
    djk = [[INF] * (n + 1) for i in range(n+1)]
    graph = [[] for i in range(n+1)]

    for fare in fares:
        src, dst, cost = fare[0], fare[1], fare[2]
        graph[src].append([dst, cost])
        graph[dst].append([src, cost])
        
    for i in range(1,n+1):
        que = deque()
        que.append(i)
        djk[i][i] = 0
        while que:
            tmp = que.popleft()
            for node in graph[tmp]:
                if djk[i][node[0]] > djk[i][tmp] + node[1]:
                    djk[i][node[0]] = djk[i][tmp] + node[1]
                    que.append(node[0])
    for i in range (1,n+1):
        if djk[s][i] + djk[i][a] + djk[i][b] < answer:
            answer = djk[s][i] + djk[i][a] + djk[i][b]
    return answer
