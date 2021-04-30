def solution(dirs):
    answer = 0
    trace = []
    cordinate = [0,0]
    for i in dirs:
        tmp = [cordinate[0],cordinate[1]]
        if i == 'U':
            if cordinate [1] != 5:
                cordinate[1] += 1
        elif i == 'D':
            if cordinate [1] != -5:
                cordinate[1] -= 1
        elif i == 'L':
            if cordinate [0] != -5:
                cordinate[0] -= 1
        else:
            if cordinate [0] != 5:
                cordinate[0] += 1
        new = tmp + cordinate
        new2 = cordinate + tmp
        if tmp != cordinate:
            if not new in trace:
                trace.append(new)
                trace.append(new2)
                answer += 1
    return answer
