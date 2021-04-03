def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    count = 0
    lost2 = []
    for i in range (len(lost)):
        check = 0
        for j in range(len(reserve)):
            if (lost[i] == reserve[j]):
                check = 1
        if (check == 0):
            lost2.append(lost[i])
    for i in range (len(lost)):
        for j in range(len(reserve)):
            if (lost[i] == reserve[j]):
                reserve.pop(j)
                break
    for i in range (len(lost2)):
        for j in range(len(reserve)):
            if (lost2[i] - 1 == reserve[j]):
                count += 1
                reserve.pop(j)
                break
            if (lost2[i] + 1 == reserve[j]):
                count += 1
                reserve.pop(j)
                break
    answer = n - (len(lost2) - count)
    return answer
