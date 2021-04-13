def solution(bridge_length, weight, truck_weights):
    answer = 0
    curr = []
    curr_weight = 0
    for i in truck_weights:
        # while curr_weight + i < weight
        check = 0
        if len(curr) > 0 :
            if curr[0][1] >= bridge_length:
                curr.pop(0)
        while curr_weight + i > weight:
            tmp = curr.pop(0)
            curr_weight -= tmp[0]
            answer += bridge_length - tmp[1]
            for j in range (len(curr)):
                curr[j][1] += bridge_length - tmp[1]
            check = 1 
        curr_weight += i
        if check != 1:
            for t in curr:
                t[1] += 1
            answer += 1
        curr.append([i,0])
    answer += bridge_length 
        
    return answer
