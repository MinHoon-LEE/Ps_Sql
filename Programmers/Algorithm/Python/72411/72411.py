from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        arr = []
        for j in orders:
            j = sorted(j)
            comb = combinations(j,i)
            arr += comb
        count = Counter(arr)
        tmp = count.values()
        if len(count) > 0:
            max_value = max(tmp)
        else:
            max_value = 0
        if len(count) > 0 and max_value > 1:
            for i in count:
                if count[i] == max_value:
                    answer.append(''.join(i))
    return sorted(answer)
