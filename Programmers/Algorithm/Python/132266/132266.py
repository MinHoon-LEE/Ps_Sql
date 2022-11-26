from collections import defaultdict
from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    global graph
    graph = defaultdict(list)
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    visited = cost(destination)
    for source in sources:
        if source in visited:
            answer.append(visited[source])
        else:
            answer.append(-1)
    return answer


def cost(start):
    global graph
    visited = defaultdict()
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        node = q.popleft()
        for new in graph[node]:
            if not new in visited:
                visited[new] = visited[node] + 1
                q.append(new)
    return visited
