def solution(s):
    answer = True
    count = 0 
    for i in range (len(s)):
        if count == 0:
            if s[i] == ')':
                return False
        if s[i] == '(':
            count += 1
        else:
            count -= 1
    if count == 0:
        return True
    else:
        return False
