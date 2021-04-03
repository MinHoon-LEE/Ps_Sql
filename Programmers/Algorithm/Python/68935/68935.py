def solution(n):
    arr = []
    while ((int)(n) != 0):
        arr.append(n % 3)
        n = (int)(n/3)
        
    sum = 0
    for i in range(len(arr)):
        sum = 3 * sum + arr[i]
    answer = sum
    return answer
