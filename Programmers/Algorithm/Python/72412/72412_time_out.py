def solution(info, query):
    answer = []
    new_info = []
    new_query = []
    for i in info:
        new_info.append(i.split(' '))
    for i in query:
        new_query.append(i.split(' and '))
    for i in new_query:
        tmp = i.pop()
        i += tmp.split(' ')
    for i in new_query:
        new_new = [0] * len(new_query)
        for j in range (len(i)):
            if i[j] == '-':
                for t in range (len(new_new)):
                    new_new[t] += 1
            else:
                if j < 4:
                    for t in range (len(new_info)):
                        if new_info[t][j] == i[j]:
                            new_new[t] += 1
                else:
                    for t in range (len(new_info)):
                        if int(new_info[t][j]) >= int(i[j]):
                            new_new[t] += 1
        count = 0
        for j in new_new:
            if j == 5:
                count += 1
        answer.append(count)
    return answer
