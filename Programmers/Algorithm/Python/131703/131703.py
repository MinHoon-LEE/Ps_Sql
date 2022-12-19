import copy
from itertools import product

def solution(beginning, target):
    answer = 1000000
    global x, y
    x = len(beginning)
    y = len(beginning[0])
    a = [0,1]
    product_x = list(product(a, repeat = x))
    for p_x in product_x:
        ## flip
        new = copy.deepcopy(beginning)
        count = 0
        for i in range (len(p_x)):
            if p_x[i] == 1:
                new = flip_row(new,i)
                count += 1
        for j in range (y):
            for i in range (x):
                if new[i][j] != target[i][j]:
                    new = flip_col(new,j)
                    count += 1
                    break
        if new == target:
            answer = min(answer,count)
    if answer == 1000000:
        return -1
    return answer

def flip_row(arr,i):
    global x,y
    for j in range (y):
        if arr[i][j] == 1:
            arr[i][j] = 0
        else:
            arr[i][j] = 1
    return arr
        
def flip_col(arr,j):
    global x,y
    for i in range (x):
        if arr[i][j] == 1:
            arr[i][j] = 0
        else:
            arr[i][j] = 1
    return arr
