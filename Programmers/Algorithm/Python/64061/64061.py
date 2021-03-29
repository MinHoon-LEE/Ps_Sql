basket = []
count = 0 

def decrane(n,board):
    i = 0
    while (i < len(board[0])):
        if (board[i][n] != 0):
            tmp = board[i][n]
            board[i][n] = 0
            return (tmp)
        i = i + 1
    return (-1)

def remove_basket():
    global count 
    i = len(basket) - 2
    if (i >= 0):
        if(basket[i] == basket[i+1]):
            del basket[i]
            del basket[i]
            count = count + 2  

def in_basket(num):
    if(num != -1):
        basket.append(num)
        remove_basket()


def solution(board, moves):
    for i in moves:
        in_basket(decrane(i - 1,board))        
    answer = count
    return answer
