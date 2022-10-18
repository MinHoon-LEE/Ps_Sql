from collections import deque
def solution(board):
    N = len(board[0])
    MAXI = 25 *25 * 6
    dp = [[[MAXI] * N for i in range(N)] for j in range(4)]
    
    direction = [[1,0,0],[0,1,1],[-1,0,2],[0,-1,3]]
    que = deque()
    que.append([0,0,0,0])# (x,y,cost,direction)
    que.append([0,0,0,1])
    while que:
        tmp = que.popleft()
        for direct in direction:
            next_x = tmp[0] + direct[0]
            next_y = tmp[1] + direct[1]
            next_direct = direct[2]
            next_cost = tmp[2] + 1
            if next_direct != tmp[3]:
                next_cost += 5
            if next_x >= 0 and next_x < N and next_y >=0 and next_y < N and dp[next_direct][next_x][next_y] > next_cost and board[next_x][next_y] == 0:
                dp[next_direct][next_x][next_y] = next_cost
                que.append([next_x,next_y,next_cost,next_direct])

    return min(dp[0][N-1][N-1],dp[1][N-1][N-1]) * 100
