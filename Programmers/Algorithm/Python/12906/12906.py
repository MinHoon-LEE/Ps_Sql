def solution(arr):
    answer = []
    tmp = ''
    for i in arr:
        if(tmp != i):
            answer.append(i)
            tmp = i
    return answer
