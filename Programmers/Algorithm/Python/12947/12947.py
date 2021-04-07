def solution(x):
    tmp = list(str(x))
    sum = 0
    for i in tmp:
        sum += int(i)
    if (x % sum == 0 ):
        return True
    else:
        return False
