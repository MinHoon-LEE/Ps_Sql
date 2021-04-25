def find(n,m,maps):
    value = maps[n][m]
    if n - 1 >=0 :
        if maps[n-1][m] != 0:
            if maps[n-1][m] != 1:
                if maps[n-1][m] > value + 1:
                    maps[n-1][m] = value + 1
                    find(n-1,m,maps)
            else:
                maps[n-1][m] = value + 1
                find(n-1,m,maps)
    if n + 1 < len(maps):
        if maps[n+1][m] != 0:
            if maps[n+1][m] != 1:
                if maps[n+1][m] > value + 1:
                    maps[n+1][m] = value + 1
                    find(n+1,m,maps)
            else:
                maps[n+1][m] = value + 1
                find(n+1,m,maps)
    if m - 1 >=0:
        if maps[n][m-1] != 0:
            if maps[n][m-1] != 1:
                if maps[n][m-1] > value + 1:
                    maps[n][m-1] = value + 1
                    find(n,m-1,maps)
            else:
                maps[n][m-1] = value + 1
                find(n,m-1,maps)
    if m + 1 < len(maps[0]):
        if maps[n][m+1] != 0:
            if maps[n][m+1] != 1:
                if maps[n][m+1] > value + 1:
                    maps[n][m+1] = value + 1
                    find(n,m+1,maps)
            else:
                maps[n][m+1] = value + 1
                find(n,m+1,maps)
        

def solution(maps):
    answer = 0
    find(0,0,maps)
    if maps[len(maps)-1][len(maps[0])-1] == 1:
        return -1
    else:
        return maps[len(maps)-1][len(maps[0])-1]
