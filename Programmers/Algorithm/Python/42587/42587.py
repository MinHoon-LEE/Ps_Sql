def solution(priorities, location):
    answer = 1
    priorities2 = []
    for idx,i in enumerate(priorities):
        if (location == idx):
            priorities2.append([i,1])
        else:
            priorities2.append([i,0])
    while(1):
        stat = 0
        tmp = priorities2.pop(0)
       # print(tmp)
        for i in priorities2:
            if not tmp[0] >= i[0]:
                priorities2.append(tmp)
                stat = 1
                break 
        if (stat == 0):
            print(tmp)
            if (tmp[1] == 1):
                return answer
            answer += 1
    return answer
