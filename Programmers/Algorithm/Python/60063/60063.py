from collections import defaultdict
import copy

def search(weak,i):
    global answer, dist
    
    for w in weak:
        tmp = []
        for j in weak:
            if not((j>= w and j<=w+dist[i]) or (j+n>= w and j + n <= w+dist[i])):
                tmp.append(j)
        if tmp == []:
            answer = i
            return
        if i <= answer+1:
            return
        search(tmp,i-1)
        
def solution(n1, weak, dist1):
    global dist, n,answer
    n = n1 
    dist = dist1
    i = len(dist) - 1
    answer = -1
    search(weak,i)
    if answer == -1:
        return -1
    return i - answer + 1
