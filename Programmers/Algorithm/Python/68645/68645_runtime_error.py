def solution(n):
    answer = []
    sum = int((n / 2) * (n + 1))
    for i in range (1,n+1):
        answer.append([0] * i)
    c_i= [1,1]
    for i in range (1,n+1):
        answer[i-1][0] = i
    for i in range (1,n):
        answer[n-1][i] = n + i
    for i in range (1, n - 1):
        answer[n-1-i][n-1-i] = 2 * n + i - 1
    n -= 1
    for i in range (answer[1][1], sum + 1):
        answer[c_i[0]][c_i[1]] = i
        if c_i[0] + 1 < n:
            c_i[0] += 1
        else:
            n -= 1
            if answer[c_i[0]][c_i[1] + 1] == 0:
                c_i[1] +=1
            else:
                if answer[c_i[0] - 1][c_i[1] - 1] == 0:
                    c_i[0] -= 1
                    c_i[1] -= 1
                else:
                    c_i[0] += 1
    tmp = []
    for i in answer:
        for j in i:
            tmp.append(j)
    return tmp
