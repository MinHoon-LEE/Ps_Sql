def solution(absolutes, signs):
    answer = 0
    for i in range (len(absolutes)):
        tmp = absolutes[i]
        if signs[i] == False:
            tmp = -tmp
        answer += tmp
    return answer
