def solution(numbers):
    answer = ''
    new = []
    max_len = 0
    numbers.sort()
    numbers.reverse()
    for i in numbers:
        new.append([str(i) * 4,str(i)])
    numbers.sort()
    new = sorted(new,key = lambda x :x[0])    
    new.reverse()
    for i in new:
        answer += str(i[1])
    return str(int(answer))
