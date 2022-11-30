from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board = [[ -1 for i in range (202)] for i in range(202)]
    dp = [[100000 for i in range(202)] for i in range(202)]
    for x1,y1,x2,y2 in rectangle:
        for i in range (2*x1,2*x2+1):
            for j in range (2*y1,2*y2+1):
                if i == 2*x1 or i == 2*x2 or j == 2*y1 or j == 2*y2:
                    if board[i][j] == -1 or board[i][j] == 1:
                        board[i][j] = 1      
                else:
                    board[i][j] = 0     
    q = deque()
    q.append([2*characterX,2*characterY])
    dp[2*characterX][2*characterY] = 0
    while q:
        x,y = q.popleft()
        tmp = [[x,y+1],[x,y-1],[x+1,y],[x-1,y]]
        for a,b in tmp:
            if board[a][b] == 1:
                if dp[a][b] > dp[x][y] + 1:
                    dp[a][b] = dp[x][y] + 1
                    q.append([a,b])
    return dp[2*itemX][2*itemY] /2 
