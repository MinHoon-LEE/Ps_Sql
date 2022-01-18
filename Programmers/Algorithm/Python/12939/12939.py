def solution(s):
    answer = ''
    i = 0 
    minus_flag = 0 
    first_flag = 0
    tmp = 0
    while i < len(s):
        if s[i] == '-':
            minus_flag = 1
        if s[i].isdigit():
            tmp = 10 * tmp + int(s[i])
            print(tmp)
        if s[i] == ' ' or i == len(s) - 1:
            if minus_flag == 1:
                tmp = -tmp
                minus_flag = 0
            if first_flag == 0:
                max = tmp
                min = tmp
                first_flag = 1
            if tmp > max:
                max = tmp
            if tmp < min:
                min = tmp
            tmp = 0
        i += 1
    return str(min) + " " + str(max)
