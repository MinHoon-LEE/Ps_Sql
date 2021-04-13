def solution(bridge_length, weight, truck_weights):
    answer = 0
    curr_weight = 0
    arr = [0] * bridge_length
    while truck_weights:
        answer += 1
        tmp = truck_weights[0]
        curr_weight -= arr.pop(0)
        if curr_weight + tmp > weight:
            arr.append(0)
        else:
            truck_weights.pop(0)
            arr.append(tmp)
            curr_weight += tmp
    answer += bridge_length
        
    return answer
