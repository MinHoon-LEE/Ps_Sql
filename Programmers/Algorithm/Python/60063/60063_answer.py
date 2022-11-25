from collections import deque 
from collections import defaultdict

def solution(board):
    answer = 0
    dp = [[[[1000000 for i in range(len(board)) ]for i in range (len(board)) ]for i in range(len(board))] for i in range(len(board))]
    dp[0][0][0][1] = 0
    q = deque()
    q.append([[0,0],[0,1]])
    
    while q:
        a, b = q.popleft()
        ## 6가지 움직임
        m = [b[0] - a[0], b[1] - a[1]]
        ## 앞/뒤 움직임
        # 앞
        new_a = [a[0] + 1,a[1]]
        new_b = [b[0] + 1,b[1]]
        if check(len(board),new_b) == 1 and board[new_b[0]][new_b[1]] == 0 and board[new_a[0]][new_a[1]] == 0:
            if dp[new_a[0]][new_a[1]][new_b[0]][new_b[1]] > dp[a[0]][a[1]][b[0]][b[1]] + 1:
                dp[new_a[0]][new_a[1]][new_b[0]][new_b[1]] = dp[a[0]][a[1]][b[0]][b[1]] + 1
                q.append([new_a,new_b])
        new_a = [a[0] - 1,a[1]]
        new_b = [b[0] - 1,b[1]]
        if check(len(board),new_a) == 1 and board[new_b[0]][new_b[1]] == 0 and board[new_a[0]][new_a[1]] == 0:
            if dp[new_a[0]][new_a[1]][new_b[0]][new_b[1]] > dp[a[0]][a[1]][b[0]][b[1]] + 1:
                dp[new_a[0]][new_a[1]][new_b[0]][new_b[1]] = dp[a[0]][a[1]][b[0]][b[1]] + 1
                q.append([new_a,new_b])
        new_a = [a[0] ,a[1] + 1]
        new_b = [b[0] ,b[1] + 1]
        if check(len(board),new_b) == 1 and board[new_b[0]][new_b[1]] == 0 and board[new_a[0]][new_a[1]] == 0:
            if dp[new_a[0]][new_a[1]][new_b[0]][new_b[1]] > dp[a[0]][a[1]][b[0]][b[1]] + 1:
                dp[new_a[0]][new_a[1]][new_b[0]][new_b[1]] = dp[a[0]][a[1]][b[0]][b[1]] + 1
                q.append([new_a,new_b])
        new_a = [a[0] ,a[1] - 1]
        new_b = [b[0] ,b[1] - 1]
        if check(len(board),new_a) == 1 and board[new_b[0]][new_b[1]] == 0 and board[new_a[0]][new_a[1]] == 0:
            if dp[new_a[0]][new_a[1]][new_b[0]][new_b[1]] > dp[a[0]][a[1]][b[0]][b[1]] + 1:
                dp[new_a[0]][new_a[1]][new_b[0]][new_b[1]] = dp[a[0]][a[1]][b[0]][b[1]] + 1
                q.append([new_a,new_b])     
        if m[0] == 1:
            #a기준
                #1
            new_a = [a[0], a[1] + 1]
            if check(len(board), new_a) == 1 and board[new_a[0]][new_a[1]] == 0 and board[b[0]][b[1]+1] == 0:
                if dp[a[0]][a[1]][new_a[0]][new_a[1]] > dp[a[0]][a[1]][b[0]][b[1]] + 1:
                    dp[a[0]][a[1]][new_a[0]][new_a[1]] = dp[a[0]][a[1]][b[0]][b[1]] + 1
                    q.append([a,new_a])
                #2
            new_a = [a[0], a[1] - 1]
            if check(len(board), new_a) == 1 and board[new_a[0]][new_a[1]] == 0 and board[b[0]][b[1]-1] == 0:
                if dp[new_a[0]][new_a[1]][a[0]][a[1]] > dp[a[0]][a[1]][b[0]][b[1]] + 1:
                    dp[new_a[0]][new_a[1]][a[0]][a[1]] = dp[a[0]][a[1]][b[0]][b[1]] + 1
                    q.append([new_a,a])
            #b기준
                #1
            new_a = [b[0], b[1] + 1]
            if check(len(board), new_a) == 1 and board[new_a[0]][new_a[1]] == 0 and board[a[0]][a[1]+1] == 0:
                if dp[b[0]][b[1]][new_a[0]][new_a[1]] > dp[a[0]][a[1]][b[0]][b[1]] + 1:
                    dp[b[0]][b[1]][new_a[0]][new_a[1]] = dp[a[0]][a[1]][b[0]][b[1]] + 1
                    q.append([b,new_a])
                #2
            new_a = [b[0], b[1] - 1]
            if check(len(board), new_a) == 1 and board[new_a[0]][new_a[1]] == 0 and board[a[0]][a[1]-1] == 0:
                if dp[new_a[0]][new_a[1]][b[0]][b[1]] > dp[a[0]][a[1]][b[0]][b[1]] + 1:
                    dp[new_a[0]][new_a[1]][b[0]][b[1]] = dp[a[0]][a[1]][b[0]][b[1]] + 1
                    q.append([new_a,b])
        if m[1] == 1:
            #a기준
                #1
            new_a = [a[0] + 1,a[1]]
            if check(len(board), new_a) == 1 and board[new_a[0]][new_a[1]] == 0 and board[b[0] +1][b[1]] == 0:
                if dp[a[0]][a[1]][new_a[0]][new_a[1]] > dp[a[0]][a[1]][b[0]][b[1]] + 1:
                    dp[a[0]][a[1]][new_a[0]][new_a[1]] = dp[a[0]][a[1]][b[0]][b[1]] + 1
                    q.append([a,new_a])
                #2
            new_a = [a[0] - 1,a[1]]
            if check(len(board), new_a) == 1 and board[new_a[0]][new_a[1]] == 0 and board[b[0] -1][b[1]] == 0:
                if dp[new_a[0]][new_a[1]][a[0]][a[1]] > dp[a[0]][a[1]][b[0]][b[1]] + 1:
                    dp[new_a[0]][new_a[1]][a[0]][a[1]] = dp[a[0]][a[1]][b[0]][b[1]] + 1
                    q.append([new_a,a])
            #b기준
                #1
            new_a = [b[0] + 1,b[1]]
            if check(len(board), new_a) == 1 and board[new_a[0]][new_a[1]] == 0 and board[a[0] +1][a[1]] == 0:
                if dp[b[0]][b[1]][new_a[0]][new_a[1]] > dp[a[0]][a[1]][b[0]][b[1]] + 1:
                    dp[b[0]][b[1]][new_a[0]][new_a[1]] = dp[a[0]][a[1]][b[0]][b[1]] + 1
                    q.append([b,new_a])
                #2 
            new_a = [b[0] - 1,b[1]]
            if check(len(board), new_a) == 1 and board[new_a[0]][new_a[1]] == 0 and board[a[0] -1][a[1]] == 0:
                if dp[new_a[0]][new_a[1]][b[0]][b[1]] > dp[a[0]][a[1]][b[0]][b[1]] + 1:
                    dp[new_a[0]][new_a[1]][b[0]][b[1]] = dp[a[0]][a[1]][b[0]][b[1]] + 1
                    q.append([new_a,b])
    return min(dp[len(board)-1][len(board)-2][len(board)-1][len(board)-1],dp[len(board)-2][len(board)-1][len(board)-1][len(board)-1])

def check(n,arr):
    if arr[0] < 0 or arr[0] >= n:
        return -1
    if arr[1] < 0 or arr[1] >= n:
        return -1
    return 1
