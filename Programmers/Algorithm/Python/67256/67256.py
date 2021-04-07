def distance(a,b):
    return abs(a[0] - b[0]) + abs(a[1]-b[1])

def find_index(number):
    index_list = []
    arr = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if (arr[i][j] == number):
                index_list = [i,j]
                return index_list

def solution(numbers, hand):
    answer = ''
    L_index = [3,0]
    R_index = [3,2]
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            L_index = find_index(i)
        elif i in [3,6,9]:
            answer += 'R'
            R_index = find_index(i)
        else:
            tmp = find_index(i)
            if (distance(L_index,tmp) < distance(R_index,tmp)):
                answer += 'L'
                L_index = tmp
            elif (distance(L_index,tmp) > distance(R_index,tmp)):
                answer += 'R'
                R_index = tmp
            else:
                if (hand == 'right'):
                    answer += 'R'
                    R_index = tmp
                else:
                    answer += 'L'
                    L_index = tmp
    return answer
