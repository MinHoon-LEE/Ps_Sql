def solution(tickets):
    answer = []
    dic = defaultdict(list)
    for ticket in tickets:
        dic[ticket[0]].append(ticket[1])
    for i in dic:
        dic[i].sort()
    num = 0
    airport = "ICN"
    que = deque()
    que.append(airport)
    while que:
        tmp = que.pop()
        if tmp not in dic or not dic[tmp]:
            answer.append(tmp)
        else:
            que.append(tmp)
            que.append(dic[tmp].pop(0))
            
    return answer[::-1]
