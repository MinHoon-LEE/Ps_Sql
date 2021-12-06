def solution(n):
    answer = 0
    for i in range(1, n + 1):
        tmp = 0
        num = i
        while (1):
            tmp += num
            if tmp == n:
                answer += 1
                break
            if tmp > n:
                break
            num += 1
    return answer
