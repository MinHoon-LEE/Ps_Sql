def solution(s):
    s = list(s)
    min_length = len(s)
    for i in range (1,len(s) // 2 + 1):
        curr = []
        count = 1
        answer = []
        for j in range (0,len(s) // i):
            tmp = s[j * i: (j + 1) * i]
            if curr == tmp:
                count += 1
            else:
                if count > 1:
                    answer.append(count)
                for t in curr:
                    answer.append(t)
                curr = tmp
                count = 1
        if count > 1:
            answer.append(count)
        for t in curr:
            answer.append(t)
        for q in range ((j + 1) * i, len(s)):
            answer.append(s[q])
        tmp = ""
        for o in  answer:
            tmp += str(o)
        if min_length > len(tmp):
            min_length = len(tmp)
    return min_length
