from collections import deque

def solution(maps):
    answer = 0
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    queue = deque([[0,0,1]])
    w = len(maps)
    e = len(maps[0])
    while queue:
        tmp = queue.popleft()
        x  = tmp[0]
        y  = tmp[1]
        value = tmp[2]
        for xi, yi in dirs:
            tmp_x = x + xi
            tmp_y = y + yi
            if tmp_x == w-1 and tmp_y == e-1:
                return value + 1
            if 0 <= tmp_x < w and 0<= tmp_y < e and maps[tmp_x][tmp_y] == 1:
                maps[tmp_x][tmp_y] = 0
                queue.append([tmp_x,tmp_y,value+1])
    return -1
