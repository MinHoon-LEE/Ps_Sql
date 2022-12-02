from collections import deque
import copy
import sys
sys.setrecursionlimit(10**6)

def solution(board, r, c):
    global answer, clear_board
    clear_board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    answer = 100000
    for i in range (4):
        for j in range(4):
            if board[i][j] != 0:
                cnt = p_to_p(board,i,j,r,c)
                dfs(board,i,j,cnt)
    return answer

def dfs(board,x,y, cnt):
    global answer
    new_board = copy.deepcopy(board)
    for i in range (4):
        for j in range (4):
            if [x,y] != [i,j] and new_board[i][j] == new_board[x][y]:
                n_i = i
                n_j = j
    cnt += p_to_p(new_board,x,y,n_i,n_j) + 2
    new_board[x][y] = 0
    new_board[n_i][n_j] = 0
    if new_board == clear_board:
        answer = min(cnt,answer)
    for i in range(4):
        for j in range(4):
            if new_board[i][j] != 0:
                plus = p_to_p(new_board,n_i,n_j,i,j)
                dfs(new_board,i,j,cnt+plus)

def p_to_p(board,x1,y1,x2,y2):
    q = deque()
    dp = [[100 for i in range (4)] for i in range (4)]
    dp[x1][y1] = 0
    q.append([x1,y1])
    while q:
        a,b = q.popleft()
        if a == x2 and b == y2:
            return dp[x2][y2]
        arr = [[0,1],[0,-1],[1,0],[-1,0]]
        for dx,dy in arr:
            new_x, new_y = a + dx, b + dy
            if 0 <= new_x < 4 and 0 <= new_y < 4:
                if dp[new_x][new_y] > dp[a][b] + 1:
                    dp[new_x][new_y] = dp[a][b] + 1
                    q.append([new_x,new_y])
        for dx,dy in arr:
            new_x, new_y = a, b
            while 0 <= new_x + dx < 4 and 0 <= new_y + dy < 4:
                new_x, new_y = new_x + dx, new_y + dy
                if board[new_x][new_y] != 0:
                    break
            if dp[new_x][new_y] > dp[a][b] + 1:
                dp[new_x][new_y] = dp[a][b] + 1
                q.append([new_x,new_y])
