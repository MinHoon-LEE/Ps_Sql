def calculate(a, b):
    res = 1
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            res = i
    return a * b // res

def solution(arr):
    
    arr = sorted(arr)
    answer = arr[0]
    for i in range(1, len(arr)):
         answer = calculate(answer, arr[i])
    return answer
