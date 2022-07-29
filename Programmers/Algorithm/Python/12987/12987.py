def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        if find_num(A[i],B) == 1:
            answer += 1
    return answer

def find_num(n, arr):
    win_flag = 0
    for i in range(len(arr)):
        if arr[i] > n:
            win_flag = 1
            break;
    if win_flag == 1:
        arr.remove(arr[i])
        return 1
    arr.remove(arr[0])
    return 0
