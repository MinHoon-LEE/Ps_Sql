from datetime import datetime

def solution(m, musicinfos):
    answer = ''
    time1 = 0
    for musics in musicinfos:
        music = musics.split(',')
        time = []
        time.append(music[0].split(':'))
        time.append(music[1].split(':'))
        hour = int(time[1][0]) - int(time[0][0])
        minute = int(time[1][1]) - int(time[0][1])
        count = hour * 60 + minute
        new = ""
        tmp = 0
        for i in range(count):
            new += music[3][tmp % len(music[3])]
            tmp += 1
            if music[3][tmp % len(music[3])] == '#':
                new += music[3][tmp % len(music[3])]
                tmp += 1
        length = len(m)
        i = 0
        index = 1
        while(1):
            index = new.find(m,i)
            if index == -1:
                break
            if index + length < len(new):
                if not new[index + length] == '#':
                    if time1 < count:
                        time1 = count
                        answer = music[2]
            else:
                if time1 < count:
                        time1 = count
                        answer = music[2]
            i += 1
    if time1 == 0:
        return "(None)"
    return answer
