def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    if int(sum ** 0.5) != sum ** 0.5:
        tmp = int(sum ** 0.5) + 1
    else:
        tmp = int(sum ** 0.5)
    for i in  range (tmp,sum):
        if sum % i == 0:
            j = sum / i
            if 2 * (i + j) == brown + 4 and (i - 2) * (j- 2) == yellow:
                return [i,j]
