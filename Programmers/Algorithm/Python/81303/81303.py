from collections import defaultdict
from collections import deque

def solution(n, k, cmds):
    answer = ''
    length = n
    curr = k
    curr_delete = deque()
    left_que = []
    next_arr = [-1] * n
    prev_arr = [-1] * n
    for i in range(n):
        left_que.append(i)
    for i in range(n-1):
        next_arr[i] = i + 1
        prev_arr[i+1] = i
    for cmd in cmds:
        tmp = cmd.split()
        if tmp[0] == 'D':
            for i in range(int(tmp[1])):
                curr = next_arr[curr]
        elif tmp[0] == 'U':
            for i in range(int(tmp[1])):
                curr = prev_arr[curr]
        elif tmp[0] == 'C':
            curr_delete.append(curr)
            if next_arr[curr] == -1:
                next_arr[prev_arr[curr]] = -1
                curr = prev_arr[curr]
            else:
                if prev_arr[curr] == -1:
                    prev_arr[next_arr[curr]] = -1
                else:
                    next_arr[prev_arr[curr]] = next_arr[curr]
                    prev_arr[next_arr[curr]] = prev_arr[curr]
                curr = next_arr[curr]
        elif tmp[0] == 'Z':
            tmp = curr_delete.pop()
            if prev_arr[tmp] != -1:
                next_arr[prev_arr[tmp]] = tmp
            if next_arr[tmp] != -1:
                prev_arr[next_arr[tmp]] = tmp
    answer = ['O'] * n
    for i in curr_delete:
        answer[i] = 'X'
    return ''.join(answer)
