from collections import defaultdict

def solution(n, build_frame):
    answer = []
    pill_point_arr = defaultdict()
    line_point_arr = defaultdict()
    for x,y,a,b in build_frame:
        # 삭제
        if b == 0:
            if a == 0:
                no_flag = 0 
                if (x,y+2) in pill_point_arr:
                    if not (x,y+1) in line_point_arr and not(x-1,y+1) in line_point_arr:
                        no_flag = 1
                if (x,y+1) in line_point_arr:
                    if not ((x+1,y+1) in pill_point_arr or ((x+1,y+1) in line_point_arr and (x-1,y+1) in line_point_arr)):
                            no_flag = 1
                if (x-1,y+1) in line_point_arr:
                    if not ((x-1,y+1) in pill_point_arr or ((x,y+1) in line_point_arr and (x-2,y+1) in line_point_arr)):
                            no_flag = 1
                if no_flag == 0:
                    pill_point_arr.pop((x,y+1))

            if a == 1:
                no_flag = 0
                if (x-1,y) in line_point_arr:
                    if not ((x,y) in pill_point_arr or (x-1,y) in pill_point_arr):
                        no_flag = 1
                if (x,y+1) in pill_point_arr:
                    if not ((x,y) in pill_point_arr  or (x-1,y) in line_point_arr):
                        no_flag = 1
                if (x+1,y) in line_point_arr:
                    if not ((x+1,y) in pill_point_arr or (x+2,y) in pill_point_arr):
                        no_flag = 1
                if (x+1,y+1) in pill_point_arr:
                    if not ((x+1,y) in pill_point_arr or (x+1,y) in line_point_arr):
                        no_flag = 1
                if no_flag == 0:
                    line_point_arr.pop((x,y))
                
        # 설치
        if b == 1:
            if a == 0:
                # 바닥 설치
                if y == 0:
                    pill_point_arr[(x,y+1)] = 1
                # 바닥 아닌 설치
                else:  
                    if (x,y) in line_point_arr or (x-1,y) in line_point_arr or (x,y) in pill_point_arr:
                        pill_point_arr[(x,y+1)] = 1
            if a == 1:
                # 상관없이 설치
                if (x,y) in pill_point_arr or (x+1,y) in pill_point_arr:
                    line_point_arr[(x,y)] = 1
                else:
                    if (x+1,y) in line_point_arr and (x-1,y) in line_point_arr:
                        line_point_arr[(x,y)] = 1
    for x,y in pill_point_arr:
        answer.append([x,y-1,0])
    for x,y, in line_point_arr:
        answer.append([x,y,1])
    answer = sorted(answer, key = lambda x: (x[0],x[1],x[2]))
    return answer
