def solution(n):
    arr = list(str(n))
    arr.sort()
    arr.reverse()
    answer = ''
    for i in arr:
        answer += i
    answer = int(answer)
    return answer
