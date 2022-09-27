def solution(n, money):
    answer = 0
    arr = [1] + [0] * n
    for i in money:
        for j in range (i,n+1):
            arr[j] += arr[j-i]     
    return arr[n]
