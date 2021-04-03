def solution(a, b):
    answer = 0
    if (a > b):
        tmp = a
        a = b
        b = tmp
    while(a <= b):
        answer += a
        a = a+1
    return answer
