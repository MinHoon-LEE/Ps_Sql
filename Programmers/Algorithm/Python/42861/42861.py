def solution(n, costs):
    answer = 0
    arr = [i for i in range (n)]
    find_arr = [0]    
    costs = sorted(costs, key = lambda x:x[2])
    while len(find_arr) < n:
        for i in costs:
            if i[0] in find_arr and i[1] not in find_arr:
                find_arr.append(i[1])
                answer += i[2]
                break
            elif i[1] in find_arr and i[0] not in find_arr:
                find_arr.append(i[0])
                answer += i[2]
                break
    return answer
