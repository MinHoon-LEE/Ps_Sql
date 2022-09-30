def solution(routes):
    answer = 1
    routes = sorted(routes)
    tmp = routes[0]
    for i in range (1,len(routes)):
        if routes[i][0] <= tmp[1]:
            if routes[i][1] <= tmp[1]:
                tmp[1] = routes[i][1]
            tmp[0] = routes[i][0]
        else:
            tmp = routes[i]
            answer += 1
    return answer
