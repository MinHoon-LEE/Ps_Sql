from itertools import combinations 
from collections import defaultdict
def solution(info, query):
    answer = []
    dic = defaultdict(list)
    for i in info:
        info_ = i.split()
        tmp = int(info_[-1])
        nfo_ = info_[:-1]
        for j in range (0,5):
            combi = combinations(info_,j)
            for t in combi:
                word = ''.join(t)
                #if word in dic:
                dic[word].append(tmp)
               # else:
                #    dic[word] = [tmp]
    for key in dic:
        dic[key].sort()
    
    for q in query:
        arr = q.split()
        value = int(arr[-1])
        que = arr[:-1]
        for i in range(3):
            que.remove('and')
        while '-' in que:
            que.remove('-')
        array = dic[''.join(que)]
        start = 0
        end = len(array)
        if not array:
            answer.append(0)
        else:
            while start < end:
                index = (start + end) // 2
                if array[index] >= value:
                    end = index
                else:
                    start = index + 1
            answer.append(len(array) - end)
            
    return answer
