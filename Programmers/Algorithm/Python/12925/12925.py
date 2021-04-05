def solution(s):
    answer = 0
    for i in s:
        if (i.isdigit() == True):
            answer = 10 * answer + int(i)
    if (s[0] == '-'):
        answer = -answer
    return answer
