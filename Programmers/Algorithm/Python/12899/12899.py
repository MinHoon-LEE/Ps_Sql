def solution(n):
    answer = ''
    arr = []
    i = 1 
    while n > 0:
        tmp = n % (3**i)
        if tmp == 0:
            n -= (3 ** i)
            tmp = 4
        else:
            n -= tmp
            tmp = tmp // (3**(i-1))
        arr.append(tmp)
        i += 1
    arr.reverse()
    for i in arr:
        answer += str(i)
    return answer
