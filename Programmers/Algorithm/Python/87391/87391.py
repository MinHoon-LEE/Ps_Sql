# n = 1000,m = 1000 x=1,y=1 query = [[0,100001],[2,100001]]

from collections import deque
from collections import defaultdict
from collections import Counter

def solution(n, m, x, y, queries):
    answer = defaultdict()
    queries = queries[::-1]
    q = []
    q.append([x,y,x,y,x,y,x,y])
    for direction, dx in queries:
        for x1,y1,x2,y2,x3,y3,x4,y4 in q:
            if direction == 0:
                if y1 == 0:
                    y2 = min(y2+dx,m-1)
                    y4 = y2
                else:
                    if y1+dx > m-1 and y2+dx > m-1:
                        return 0
                    y1 = min(y1+dx,m-1)
                    y2 = min(y2+dx,m-1)
                    y3 = y1
                    y4 = y2
            elif direction == 1:
                if y2 == m - 1:
                    y1 = max(y1-dx,0)
                    y3 = y1
                else:
                    if y1-dx < 0 and y2 -dx < 0:
                        return 0
                    y1 = max(y1-dx,0)
                    y2 = max(y2-dx,0)
                    y3 = y1
                    y4 = y2
            elif direction == 2:
                if x1 == 0:
                    x3 = min(x3+dx,n-1)
                    x4 = x3
                else:
                    if x1+dx > n-1 and x3+dx > n-1:
                        return 0
                    x1 = min(x1+dx,n-1)
                    x3 = min(x3+dx,n-1)
                    x2 = x1
                    x4 = x3
            elif direction == 3:
                if x3 == n - 1:
                    x1 = max(x1-dx,0)
                    x2 = x1
                else:
                    if x1-dx < 0 and x3-dx < 0:
                        return 0
                    x1 = max(x1-dx,0)
                    x3 = max(x3-dx,0)
                    x2 = x1
                    x4 = x3
            
            q = [[x1,y1,x2,y2,x3,y3,x4,y4]]
    return (x3-x1+1) * (y2-y1+1)
