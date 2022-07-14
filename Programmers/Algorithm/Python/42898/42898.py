def solution(m, n, puddles):
    answer = 0
    dp = [[0] * (n+1) for i in range(m+1)]
    for i in range(1,m+1):
        for j in range (1,n+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            else:
                if [i,j] not in puddles:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m][n] % 1000000007
