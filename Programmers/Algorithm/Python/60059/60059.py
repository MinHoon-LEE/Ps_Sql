import copy
def solution(key, lock):
    answer = False
    
    #Lock 부분 홈/돌기 반전 
    check = 0 
    for i in range (len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                lock[i][j] = 1
                check = 1
            else:
                lock[i][j] = 0
    if check == 0:
        return True
    # 회전 x 
    if find(key,lock) == True:
        return True
    # 90도 회전
    key = rotate_90(key)
    if find(key,lock) == True:
        return True
    # 180도 회전
    key = rotate_90(key)
    if find(key,lock) == True:
        return True
    # 270도 회전 
    key = rotate_90(key)
    if find(key,lock) == True:
        return True
    
    return answer


def rotate_90(arr):
    tmp = [[0] * len(arr) for i in range (len(arr))]
    for i in range (len(arr)):
        for j in range (len(arr)):
            tmp[j][len(arr) - 1 - i] = arr[i][j]
    return tmp
    
def find(key, lock):
    length = len(lock)
    for i in range (len(lock)):
        for j in range (len(lock)):
            if move_arr(key, i, j,length) == lock:
                return True
            if move_arr(key, -i, j,length) == lock:
                return True
            if move_arr(key, i, -j,length) == lock:
                return True
            if move_arr(key, -i, -j,length) == lock:
                return True
    return False 

def move_arr(arr, i ,j,length):
    tmp =  [[0] * length for r in range (length)]
    for a in range (len(arr)):
        for b in range (len(arr)):
            if a + i < length and a + i >= 0:
                if b + j < length and b + j >= 0:
                    tmp[a+i][b+j] = arr[a][b]
    return tmp
