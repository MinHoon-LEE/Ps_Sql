def solution(board, skill):
    answer = 0
    length = len(board) + 1
    height = len(board[0]) + 1
    imos_arr = [[0 for _ in range (height)] for _ in range(length)]
    for types, r1, c1, r2, c2, degree in skill:
        if types == 1:
            types = -1
        else:
            types = 1
        imos_arr[r1][c2+1] += -degree * types
        imos_arr[r2+1][c1] += -degree * types
        imos_arr[r2+1][c2+1] += degree * types
        imos_arr[r1][c1] += degree * types
    ## 새로 합 
    for i in range (length):
        for j in range (1,height):
            imos_arr[i][j] += imos_arr[i][j-1]
    ## 가로합
    for i in range (1,length):
        for j in range (height):
            imos_arr[i][j] += imos_arr[i-1][j]   
    for i in range (length-1):
        for j in range (height-1):
            if imos_arr[i][j] + board[i][j] >= 1:
                answer += 1
    return answer
