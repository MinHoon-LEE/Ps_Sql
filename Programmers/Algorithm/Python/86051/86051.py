from collections import defaultdict

def solution(numbers):
    answer = 0
    dic = defaultdict(str)
    for i in numbers:
        dic[i] = True
    for i in range(10):
        if not i in dic:
            answer += i  
    return answer
