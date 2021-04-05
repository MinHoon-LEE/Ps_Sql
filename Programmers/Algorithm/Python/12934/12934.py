import math

def solution(n):
    answer = 0
    if (n  == int(math.sqrt(n)) **2):
        return (math.sqrt(n)+1) ** 2
    else:
        return -1
