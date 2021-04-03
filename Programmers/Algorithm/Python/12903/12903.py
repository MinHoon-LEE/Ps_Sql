def solution(s):
    answer = ''
    len_s = len(s)
    b = (int)(len_s) % 2
    a = (int)((len_s) / 2)
    if (b == 0):
        answer += s[a-1] + s[a]
    else:
        answer += s[a]
    return answer
