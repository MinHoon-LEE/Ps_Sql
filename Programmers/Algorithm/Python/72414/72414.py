def solution(play_time, adv_time, logs):
    answer = 0
    see_time = [0] * (3600 * 101)
    for log in logs:
        time = log.split('-')
        start = hour_to_sec(time[0])
        end = hour_to_sec(time[1])
        see_time[start] += 1
        see_time[end] -= 1
    for i in range (1,3600*101):
        see_time[i] += see_time[i-1]
    adv_time = hour_to_sec(adv_time)
    play_time = hour_to_sec(play_time)
    total = 0
    for i in range(adv_time):
        total += see_time[i]
    max = total
    j = 0 
    for i in range(adv_time,play_time):
        total += see_time[i]
        total -= see_time[j]
        j += 1
        if total > max:
            max = total
            answer = j
    return sec_to_hour(answer) 

def hour_to_sec(time):
    time = time.split(":")
    return 3600 * int(time[0]) + 60 * int(time[1]) + int(time[2])

def sec_to_hour(second):
    hour_10 = second // 3600 // 10
    hour_1 = second // 3600 % 10
    minuite_10 = second % 3600 // 60 // 10
    minuite_1 = second % 3600 // 60 % 10
    sec_10 = second % 60 // 10
    sec_1 = second % 60 % 10
    return str(hour_10) + str(hour_1) + ":" + str(minuite_10) + str(minuite_1) + ":" + str(sec_10) + str(sec_1)
