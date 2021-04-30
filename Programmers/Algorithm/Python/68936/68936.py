def length(num):
    n = 1
    count = 0 
    while (1):
        if n == num:
            break
        else:
            count += 1
            n *= 2
    return count
def solution(arr):
    answer = []
    count_0 = 0
    count_1 = 0 
    n = length(len(arr))
    tmp = arr
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                count_1 += 1
            else:
                count_0 += 1
    for i in range (n): # 0, 1
        for j in range (len(arr) // 2 ** (i+1)): # 0,1 , # 0 
            for k in range (len(arr) // 2 ** (i+1)): # 0, 1 0, 1
                if arr[2*j][2*k] == 0 and arr[2*j+1][2*k] == 0 and arr[2*j][2*k+1] == 0 and arr[2*j+1][2*k+1] == 0:
                    arr[j][k] = 0
                    count_0 -= 3
                    
                elif arr[2*j][2*k] == 1 and arr[2*j+1][2*k] == 1 and arr[2*j][2*k+1] == 1 and arr[2*j+1][2*k+1] == 1:
                    arr[j][k] = 1
                    count_1 -= 3
                else:
                    arr[j][k] = -1
    return [count_0,count_1]
