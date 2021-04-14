def next(x,y,check):
    if check % 3 == 0:
        x += 1
    elif check % 3 == 1:
        y += 1
    else:
        x -= 1
        y -= 1
    return x,y

def solution(n):
    answer = []
    sum = int((n / 2) * (n + 1)) 
    for i in range (1,n+1):
        answer.append([0] * i)
    x ,y = -1 , 0
    value = 1
    check = 0
    tmp = n 
    for i in range (n):
        for j in range (tmp):
            x,y = next(x,y,check)
            answer[x][y] = value
            value += 1
        tmp -= 1
        check += 1
    new = []
    for i in answer:
        for j in i:
            new.append(j)
    return new
