from itertools import combinations_with_replacement

def solution(n, info):
    score = -1
    answer = [-1]
    i = list(combinations_with_replacement(range(0,11),n))
    for a in i:
        tmp = calculate(a, info, n)
        if tmp[0] > score:
            score = tmp[0]
            answer = tmp[1]
    return answer


def calculate(a, info, n):
    tmp = [0] * 11
    rion = 0
    peach = 0
    for i in a:
        tmp[10 - i] += 1
    for i in range(len(tmp)):
        if not (tmp[i] == 0 and info[i] == 0):
            if tmp[i] > info[i]:
                rion += 10 - i
            else:
                peach += 10 - i
    if rion > peach:
        return [rion - peach, tmp]
    else:
        return [-1, [-1]]
