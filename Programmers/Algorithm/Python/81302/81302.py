def solution(places):
    answer = []
    for arr in places:
        answer.append(keep_distance(arr))
    return answer

def keep_distance(arr):
    for i in range (len(arr)):
        for j in range (len(arr[0])):
            if arr[i][j] == 'P':
                #위
                    if i - 1 >= 0:
                        if arr[i-1][j] == 'P':
                            return 0
                        if arr[i-1][j] == 'O':
                            if i - 2 >= 0:
                                if arr[i-2][j] == 'P':
                                    return 0
                #아래
                    if i + 1 <= len(arr) - 1:
                        if arr[i+1][j] == 'P':
                            return 0
                        if arr[i+1][j] == 'O':
                            if i + 2 <= len(arr) - 1:
                                if arr[i+2][j] == 'P':
                                    return 0
                #좌
                    if j - 1 >= 0:
                        if arr[i][j-1] == 'P':
                            return 0
                        if arr[i][j-1] == 'O':
                            if j - 2 >= 0:
                                if arr[i][j-2] == 'P':
                                    return 0
                #우
                    if j + 1 <= len(arr[0]) - 1:
                        if arr[i][j+1] == 'P':
                            return 0
                        if arr[i][j+1] == 'O':
                            if j + 2 <= len(arr[0]) - 1:
                                if arr[i][j+2] == 'P':
                                    return 0
                #좌 상 
                    if i - 1 >= 0 and j - 1 >=0:
                        if arr[i-1][j-1] == 'P':
                            if not (arr[i-1][j] == 'X' and arr[i][j-1] == 'X'):
                                return 0
                #좌 하
                    if i + 1 <= len(arr) -1 and j - 1 >=0:
                        if arr[i+1][j-1] == 'P':
                            if not (arr[i][j-1] == 'X' and arr[i+1][j] == 'X'):
                                return 0
                #우 상
                    if i -1 >= 0 and j + 1 <= len(arr[0]) - 1:
                        if arr[i-1][j+1] == 'P':
                            if not (arr[i][j+1] == 'X' and arr[i-1][j] == 'X'):
                                return 0
                #우 하
                    if i + 1 <= len(arr) - 1 and j + 1 <= len(arr[0]) - 1:
                        if arr[i+1][j+1] == 'P':
                            if not (arr[i+1][j] == 'X' and arr[i][j+1] == 'X'):
                                return 0
                            
    return 1
