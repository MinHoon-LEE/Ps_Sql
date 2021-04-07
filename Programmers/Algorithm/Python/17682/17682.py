def solution(dartResult):
    arr = []
    new = []
    new_alpha = []
    answer = []
    oper = ['','','']
    arr = list(dartResult)
    status = -1
    i = 0
    while i < len(dartResult):
        if dartResult[i] in ['1','2','3','4','5','6','7','8','9','0']:
            status += 1
            if dartResult[i] == '1':
                if dartResult[i+1] == '0':
                    new.append('10')
                    i = i+1
                else:
                    new.append('1')
            else:
                new.append(dartResult[i])
        if dartResult[i] in ['S','D','T']:
            new_alpha.append(dartResult[i])
        if dartResult[i] in ['#','*']:
            oper[status] = dartResult[i]
        i = i+1
    for i in range (len(new)):
        if (new_alpha[i] == 'D'):
            answer.append(int(new[i]) ** 2)
        elif (new_alpha[i] == 'T'):
            answer.append(int(new[i]) ** 3)
        else:
            answer.append(int(new[i]))
    
    for i in range (len(oper)):
        if (oper[i] == '#'):
            answer[i] = -answer[i]
    for i in range (len(oper)):
        if (oper[i] == '*'):
            if(i == 0):
                answer[i] = 2 *answer[i]
            else:
                answer[i] = 2 *answer[i]
                answer[i - 1] = 2 *answer[i - 1]
    
    sum = answer[0] + answer[1] + answer[2]
    return sum
