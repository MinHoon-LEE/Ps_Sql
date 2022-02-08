def solution(n, wires):
    answer = n
    for wire in wires:
        tmp = wires[:]
        tmp.remove(wire)
        num = count_num(tmp, wire[0]) + 1
        if answer > abs(n - 2 * num):
            answer = abs(n - 2 * num)
    return answer

def count_num(arr, num):
    tmp = []
    left = []
    answer = 0
    for i in arr:
        if i[0] == num:
            left.append(i[1])
        elif i[1] == num:
            left.append(i[0])
        else:
            tmp.append(i)
    if left == []:
        return 0
    else:
        for j in left:
            answer += count_num(tmp, j)
        return answer + len(left)
