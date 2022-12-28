def solution(board, aloc, bloc):
    global max_x, max_y
    max_x = len(board)
    max_y = len(board[0])
    answer = -1
    result = dfs(board,aloc[0],aloc[1],bloc[0],bloc[1])
    return result[1]

def cant_move(board,x,y):
    global max_x, max_y
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    for dx, dy in direction:
        if max_x > x + dx >= 0 and max_y > y + dy >= 0 and board[x+dx][y+dy] == 1:
            return False
    return True


def dfs(board,x,y,a,b):
    global max_x, max_y
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    win_flag = False
    mini = 25 
    maxi = 0
    if cant_move(board,x,y):
        return [False, 0]
    if x == a and y == b:
        return [True, 1]
    for dx,dy in direction:
        if max_x > x + dx >= 0 and max_y > y + dy >= 0 and board[x+dx][y+dy] == 1:
            board[x][y] = 0
            result = dfs(board,a,b,x+dx,y+dy)
            board[x][y] = 1
            if result[0] == False:
                win_flag = True
                mini = min(mini,result[1])
            elif win_flag == False:
                maxi = max(maxi,result[1])
    summ = mini if win_flag else maxi
    return [win_flag, summ + 1]
