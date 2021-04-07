def solution(arr):
    if (len(arr) != 1):
        index = 0
        min = arr[0]
        for i in range(len(arr)):
            if (arr[i] < min):
                index = i
                min = arr[i]
        arr.pop(index)
        answer = arr
    else:
        answer = [-1]
    return answer
