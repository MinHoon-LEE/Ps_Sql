from collections import deque

def solution(alp, cop, problems):
    max_a = 0
    max_c = 0
    for a,c,x1,x2,x3 in problems:
        max_a = max(max_a,a)
        max_c = max(max_c,c)
    alp = min(max_a,alp)
    cop = min(max_c,cop)
    solve = [[100000 for i in range(max_c+1)] for j in range (max_a+1)]
    solve[alp][cop] = 0
    flag = 0
    q = deque()
    q.append([alp,cop])
    arr = []
    while q:
        flag = 1
        a,b = q.pop()
        tmp = []
        if solve[a][b] >= solve[max_a][max_c]:
            continue
        if (a + 1 <=max_a):
            if(solve[a+1][b] > solve[a][b] + 1):
                solve[a+1][b] = solve[a][b] + 1
                q.append([a+1,b])
        if (b + 1 <= max_c):
            if (solve[a][b+1] > solve[a][b] + 1):
                solve[a][b+1] = solve[a][b] + 1
                q.append([a,b+1])
        for x1,y1,x2,y2,cost in problems:
            if a >= x1 and b >= y1:
                tmp_a = a+x2
                tmp_b = b+y2
                if a+x2 >= max_a:
                    tmp_a = min(a+x2,max_a)
                if b+y2 >= max_c:
                    tmp_b = min(b+y2,max_c)
                if solve[tmp_a][tmp_b] > solve[a][b] + cost:
                    solve[tmp_a][tmp_b] = solve[a][b] + cost
                    if not (tmp_a == max_a and tmp_b == max_c):
                        q.append([tmp_a,tmp_b])
    return solve[max_a][max_c]
