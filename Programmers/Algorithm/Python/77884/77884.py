def measure_count(num):
    if int(num ** 0.5) ** 2 == num:
        return -1
    return 1

def solution(left, right):
    answer = 0
    for i in range (left, right + 1):
        answer += i * measure_count(i)
    return answer
