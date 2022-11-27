from collections import defaultdict
from collections import deque

def solution(a, edges):
    answer = 0
    graph = defaultdict(list)
    visited = defaultdict()
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    q = deque()
    q.append(0)
    total = a[0]
    visited[0] = 0
    length = defaultdict(list)
    parent = defaultdict()
    while q:
        node = q.popleft()
        for n in graph[node]:
            if not n in visited:
                q.append(n)
                visited[n] = visited[node] + 1
                length[visited[n]].append(n)
                parent[n] = node
                total += a[n]
    if total == 0:
        n = max(length)
        for i in reversed(range(1,n+1)):
            for node in length[i]:
                a[parent[node]] += a[node]
                answer += abs(a[node])          
        return answer
    else:
        return -1
