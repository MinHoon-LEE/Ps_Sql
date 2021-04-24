def solution(board):
    answer = 0
    if board == [[1]]:
        return 1
    for i in range (len(board) - 1):
        for j in range (len(board[0]) - 1):
            if not board[i+1][j+1] == 0:
                board[i+1][j+1] = min(board[i][j],min(board[i+1][j],board[i][j+1])) + 1
                if board[i+1][j+1] > answer:
                    answer = board[i+1][j+1]
    return answer ** 2
