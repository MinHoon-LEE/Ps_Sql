def solution(n, cores):
    answer = 0
    if n <= len(cores):
        return n
    n -= len(cores)
    ## 걸리는 최소 시간 ## 
    time = 0
    left, right = 1, 100000 * n
    while left < right:  # 이분 탐색
        mid = (left + right) // 2
        temp = 0
        for c in cores:
            temp += mid // c
        if temp >= n:
            right = mid
        else:
            left = mid + 1
    for core in cores:
        n -= (left - 1) // core
    for i in range(len(cores)):
        if left  % cores[i]  == 0:
            n -= 1
            if n == 0:
                return i+1
    return answer
