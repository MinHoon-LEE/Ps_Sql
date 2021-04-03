def solution(a, b):
    day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    sum = 0
    for i in range(a - 1):
        tmp = i + 1
        if (tmp <= 7 ):
            if (tmp == 2):
                sum += 29
            elif (tmp % 2 == 1):
                sum += 31
            else:
                sum += 30
        else:
            if (tmp % 2 == 0):
                sum += 31
            else:
                sum += 30
    sum = sum + b
    print(sum)
    answer = day[(sum - 3) % 7]
    return answer
