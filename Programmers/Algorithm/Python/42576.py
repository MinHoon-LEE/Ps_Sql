def solution(participant, completion):
    dic = {}
    for a in participant:
        if a in dic:
                dic[a] += 1
        else:
            dic[a] = 1
    for b in completion:
        dic[b] -= 1
    for a in dic:
        if (dic[a] == 1):
            return (a)
