from itertools import permutations
from collections import Counter

def solution(user_id, banned_id):
    
    permute = list(permutations(user_id,len(banned_id)))
    answer = 0
    arr = []
    for i in permute:
        flag = 0
        for j in range(len(i)):
            if compare(banned_id[j],i[j]) == 0:
                flag =1
                
        if flag == 0:
            tmp_string = ""
            for i in sorted(i):
                tmp_string += i
            arr.append(tmp_string)
    return len(Counter(arr))


def compare(i, j):
    if len(i) != len(j):
        return 0
    for x in range (len(j)):
        if not i[x] == "*":
            if not j[x] == i[x]:
                return 0
    return 1
