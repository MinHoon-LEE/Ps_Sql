from itertools import product
import copy

def solution(clockHands):
    answer = 4 * (8 ** 2)
    rotate = [0,1,2,3]
    p_arr = list(product(rotate, repeat = len(clockHands)))
    p_arr = p_arr[::-1]
    for p in p_arr:
        tmp = copy.deepcopy(clockHands)
        count = 0
        for i in range(len(p)):
            do_rotate(tmp,i, p[i])
            count += p[i]
        count += do_rest(tmp)
        if is_answer(tmp):
            answer = min(answer,count)
    return answer

def do_rotate(arr,i,num):
    arr[0][i] = (arr[0][i] + num) % 4
    arr[1][i] = (arr[1][i] + num) % 4
    if i - 1 >= 0:
        arr[0][i-1] = (arr[0][i-1] + num) % 4
    if i + 1 < len(arr):
        arr[0][i+1] = (arr[0][i+1] + num) % 4
    
def do_rest(arr):
    count = 0 
    for i in range(1,len(arr)):
        for j in range(len(arr[0])):
            num = (4 - arr[i-1][j]) % 4 
            arr[i][j] = (arr[i][j] + num) % 4
            arr[i-1][j] = (arr[i-1][j] + num) % 4
            if j - 1 >= 0:
                arr[i][j-1] = (arr[i][j-1] + num) % 4
            if j + 1 < len(arr[0]):
                arr[i][j+1] = (arr[i][j+1] + num) % 4
            if i + 1 < len(arr):
                arr[i+1][j] = (arr[i+1][j] + num) % 4
            count += num
    return count 

def is_answer(arr):
    for i in range (len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != 0:
                return False
    return True
