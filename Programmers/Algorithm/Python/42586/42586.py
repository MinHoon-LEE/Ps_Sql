def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range (len(progresses)):
            progresses[i] += speeds[i]
        tmp = 0
        if progresses[0] >= 100:
            for i in range (len(progresses)):
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    tmp +=1
            answer.append(tmp)
                
    return answer
