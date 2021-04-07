def solution(N, stages):
    answer = []
    stages.sort()
    users = len(stages)
    for i in range (1,N + 1):
        count = stages.count(i)
        if (count == 0):
            answer.append([i,0])
        else:
            answer.append([i, - count/users])
            users -= count
    answer = sorted(answer,key = lambda x :x[1])
    arr = []
    for i in range (len(answer)):
        arr.append(answer[i][0])
    return arr
