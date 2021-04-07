def convert(num,n):
    tmp = ''
    for i in range (n):
        if (num % 2 == 1):
            tmp += '#'
        else:
            tmp += ' '
        num = num // 2
    return tmp[::-1]

def solution(n, arr1, arr2):
    tmp = []
    tmp2 = []
    for i in arr1:
        tmp.append(convert(i,n))
    for i in arr2:
        tmp2.append(convert(i,n))
    answer = []
    for i in range (len(arr1)):
        new = ''
        for j in range (n):
            if(tmp[i][j] == '#' or tmp2[i][j] == '#'):
                new += '#'
            else:
                new += ' '
        answer.append(new)
    return answer
