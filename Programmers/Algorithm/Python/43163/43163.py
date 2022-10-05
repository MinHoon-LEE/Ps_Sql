from collections import defaultdict
from collections import deque

def solution(begin, target, words):
    answer = 0
    graph_dict = defaultdict(list)
    found_dict = defaultdict(int)
    for i in words:
        for j in words:
            if i != j and one_diff(i,j) == 1:
                graph_dict[i].append(j)
        found_dict[i] = 0
    dq = deque()
    for i in words:
        if begin != i and one_diff(begin, i) == 1:
            found_dict[i] = 1
            dq.append(i)
    while dq:
        tmp = dq.popleft()
        if tmp == target:
            return found_dict[tmp]
        for x in graph_dict[tmp]:
            if found_dict[x] == 0:
                found_dict[x] = found_dict[tmp] + 1
                dq.append(x)
            if x == target:
                found_dict[x]
                    
    return answer


def one_diff(i,j):
    count = 0
    for x in range(len(i)):
        if i[x] != j[x]:
            count += 1
        if count >= 2:
            return 0
    return 1
