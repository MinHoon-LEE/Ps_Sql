def list_split(p):
    u = []
    v = []
    check = 0
    flag = 1 
    for i in range(len(p)):
        tmp = p.pop(0)
        u.append(tmp)
        if tmp == '(':
            check += 1
            if i == 0:
                flag = 1
        else:
            check -= 1
            if i == 0:
                flag = -1
        if check ==0:
            break
    return u , p , flag 

def correction(u):
    u.pop(0)
    u.pop()
    for i in range(len(u)):
        if u[i] == '(':
            u[i] = ')'
        else:
            u[i] = '('
    return u 
def solution(p):
    answer = ''
    u = []
    v = []
    flag = 0
    u , v , flag = list_split(list(p))
    if flag == -1:
        u = correction(u)
    if len(v) != 0:
        tmp = solution(''.join(v))
        v = list(tmp)
    if flag == -1:
        answer = '(' + ''.join(v) + ')' + ''.join(u)
    else:
        answer = ''.join(u) + ''.join(v)
    return answer
