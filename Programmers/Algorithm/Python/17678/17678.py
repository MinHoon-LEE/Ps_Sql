from collections import deque

def solution(n, t, m, timetable):
    answer = ''
    time_que = deque()
    waiting_line = deque()
    timetable.sort()
    for time in timetable:
        time_que.append(time)
    for i in range (n):
        people_in = 0
        arrive_time = 9 * 60 + t * i
        ## BUS 가 왔을때 기다리는 줄 
        while time_que:
            tmp = time_que.popleft()
            if hour_to_minuite(tmp) <= arrive_time:
                waiting_line.append(tmp)
            else:
                time_que.appendleft(tmp)
                break
        ## 버스 태우기
        while people_in < m and waiting_line:
            tmp = waiting_line.popleft()
            last_time = tmp
            people_in += 1
        if people_in == m:
            answer = minuite_to_hour(hour_to_minuite(last_time) - 1)
        else:
            answer = minuite_to_hour(arrive_time)
    return answer

def hour_to_minuite(str):
    arr = str.split(":")
    return 60 * int(arr[0]) + int(arr[1])

def minuite_to_hour(n):
    answer = ""
    hour_10 = str(n // 60 //10)
    hour_1 = str(n//60%10)
    minuite_10 = str(n % 60 // 10)
    minuite_1 = str(n%60 % 10)
    return hour_10+hour_1 + ":" + minuite_10 + minuite_1
