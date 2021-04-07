def solution(num):
    answer = 0
    i = 0
    while i <= 499:
        if (num == 1):
            return i 
        if (num % 2  == 0):
            num = num / 2
        else:
            num = num * 3 + 1
        i = i + 1
    return -1
