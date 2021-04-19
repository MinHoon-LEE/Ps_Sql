def next_position(name, tmp, i):
    a , b = 0 ,0
    for x in range (1,len(name)):
        index = (i + x ) % len(name)
        if name[index] != tmp[index]:
            a = x
            break
    for x in range (1,len(name)):
        index = (i - x ) % len(name)
        if name[index] != tmp[index]:
            b = x
            break
    if x == len(name):
        return -1 , -1
    else:
        if a <= b :
            return a, 1
        else:
            return b, -1

def solution(name):
    answer = 0
    name = list(name)
    tmp = ['A'] * len(name)
    curr_index = 0 
    while(1):
        value = abs(ord(name[curr_index]) - ord(tmp[curr_index]))
        tmp[curr_index] = name[curr_index]
        answer += min(value, 26 - value)
        a,b = next_position(name,tmp,curr_index)
        if (tmp == name):
            break
        else:
            if b == 1:
                curr_index = (a + curr_index) % len(name)
                answer += a
            else:
                curr_index = (curr_index - a) % len(name)
                answer += a 
    return answer
