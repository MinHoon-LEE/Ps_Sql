from collections import Counter

def solution(gems):
    answer = []
    cnt = Counter(gems)
    dic = dict()
    start = 0
    minimum = len(gems)
    for i in range (len(gems)):
        if not gems[i] in dic:
            dic[gems[i]] = 1
        else:
            dic[gems[i]] += 1
        if len(dic) == len(cnt):
            while len(dic) == len(cnt):
                if dic[gems[start]] > 1:
                    dic[gems[start]] -= 1
                else:
                    del(dic[gems[start]])
                start += 1
            if i+1 - start < minimum:    
                answer = [start, i+1]
                minimum = i + 1 - start

    return answer
