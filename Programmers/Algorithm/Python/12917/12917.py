def solution(s):
    answer = ''
    arr = list(s)
    arr.sort()
    arr.reverse()
    for i in arr:
        answer += i
    return answer
