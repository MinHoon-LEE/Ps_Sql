def solution(s):
    s = s.lower()
    p_num = 0
    y_num = 0
    for i in s:
        if (i == 'p'):
            p_num += 1
        if (i == 'y'):
            y_num += 1
    if (p_num == y_num):
        return True
    else:
        return False
