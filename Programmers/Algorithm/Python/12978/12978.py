from collections import deque

def solution(N, road, K):
    distance = [500001] * (N + 1)
    distance[1] = 0
    tmp = deque([[0,1]])
    while tmp:
        a = tmp.popleft()
        for i in road:
            if i[0] == a[1] and i[2] + a[0] < distance[i[1]]:
                distance[i[1]] = i[2] + a[0]
                tmp.append([i[2]+a[0],i[1]])
            if i[1] == a[1] and i[2] + a[0] < distance[i[0]]:
                distance[i[0]] = i[2] + a[0]
                tmp.append([i[2]+a[0],i[0]])
    answer = 0
    for i in range (1,N+1):
        if distance[i] <= K:
            answer +=1 
    return answer
