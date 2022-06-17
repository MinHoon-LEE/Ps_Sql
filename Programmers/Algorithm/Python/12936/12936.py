from itertools import permutations
import math

def solution(n, k):
    answer = []
    arr = [i+1 for i in range(n)]
    k -=1 
    for i in range(n):
        tmp = math.factorial(n-1-i)
        share_num = k // tmp
        k = k % tmp
        answer.append(arr[share_num])
        arr.pop(share_num)
    return answer
