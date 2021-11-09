from itertools import permutations

def calculate(list, per):
    for i in per:
        while i in list:
            index = list.index(i)
            a , b = list[index - 1] , list[index + 1]
            if i == '*':
                cal = int(a) * int(b)
            if i == '+':
                cal = int(a) + int(b)
            if i == '-':
                cal = int(a) - int(b)
            list = list[:index - 1] + [cal] + list[index + 2:]
    return abs(list[0])

def solution(expression):
    answer = 0
    tmp = list(expression)
    tmp2 = list()
    tmp2.append("")
    i = 0 
    for j in range(len(tmp)):
        if tmp[j] == '-' or tmp[j] == '+' or tmp[j] == '*':
            tmp2.append(tmp[j])
            tmp2.append("")
            i += 2
        else:
            tmp2[i] += tmp[j]
    a = ['+','-','*']
    permutate = list(permutations(a,len(a)))
    for t in permutate:
        #print(t)
        cal = calculate(tmp2,t)
        if cal > answer:
            answer = cal
    return answer
