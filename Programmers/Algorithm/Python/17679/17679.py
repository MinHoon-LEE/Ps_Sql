def solution(m, n, board):
    answer = 0
    count = 1
    for i in range (m):
        board[i] = list(board[i])
    board = board[::-1]
    while count > 0:
        tmp = minimize(m, n, board)
        board = tmp[0]
        count = tmp[1]
        answer += count
    return answer


def minimize(m , n, board):
    count = 0 
    for i in range(m-1):
        for j in range (n-1):
            if board[i][j] != "" and board[i][j].lower() == board[i+1][j].lower() == board[i][j+1].lower() == board[i+1][j+1].lower():
                board[i][j] = board[i][j].lower()
                board[i+1][j] = board[i+1][j].lower()
                board[i][j+1] = board[i][j+1].lower()
                board[i+1][j+1] = board[i+1][j+1].lower()
    #소문자로 바꾼거 제거
    for i in range(m):
        for j in range(n):
            if board[i][j].islower():
                board[i][j] = ""
                count += 1
    #제거된 공백 내리기 
    for j in range (n):
        tmp = 0
        for i in range (m):
            if board[i][j] != "":
                board[tmp][j] = board[i][j]
                tmp += 1
        for i in range (tmp, m):
            board[i][j] = ""        
                
    
    return [board, count]
