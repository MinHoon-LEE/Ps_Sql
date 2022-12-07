def solution(matrix_sizes):
    answer = 0
    m = matrix_sizes
    dp = [[0 for i in range (len(matrix_sizes))] for i in range (len(matrix_sizes))] 
    for i in range (1,len(matrix_sizes)):
        for j in range(0,len(matrix_sizes) - i):
            tmp = []
            for k in range (j,j+i):
                tmp.append(dp[j][k] + dp[k+1][j+i] + m[j][0] * m[k][1] * m[j+i][1])
            dp[j][j+i] = min(tmp)
    return dp[0][len(m)-1]
