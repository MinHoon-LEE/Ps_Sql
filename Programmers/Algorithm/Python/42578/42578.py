def solution(clothes):
    answer = 1
    a = {}
    for i in clothes:
        tmp = i[1]
        if tmp in a:
            a[tmp] += 1
        else:
            a[tmp] = 1
    for i in a:
        answer *= (a[i] + 1)
    return answer - 1
