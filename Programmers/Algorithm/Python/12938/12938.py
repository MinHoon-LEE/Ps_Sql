def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    i = s // n
    j = s % n
    answer = [i] * n
    for x in range(j):
        answer[x] += 1
    answer.sort()
    return answer
