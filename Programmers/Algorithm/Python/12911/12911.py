def binary(num):
    count = 0
    while num > 0:
        tmp = num % 2
        num = num // 2
        if tmp == 1:
            count += 1
    return count

def solution(n):
    answer = 0
    num = binary(n)
    while(1):
        n = n + 1
        if binary(n) == num:
            return n
