from collections import defaultdict

def solution(record):
    answer = []
    dic = defaultdict(str)
    for log in record:
        tmp = log.split()
        if tmp[0] != 'Leave':
            dic[tmp[1]] = tmp[2]
    for log in record:
        tmp = log.split()
        name = dic[tmp[1]]
        logging = name + "님이 "
        if tmp[0] == 'Enter':
            logging += "들어왔습니다."
        elif tmp[0] == 'Leave':
            logging += "나갔습니다."
        if  (tmp[0] != 'Change'):
            answer.append(logging)
    return answer
