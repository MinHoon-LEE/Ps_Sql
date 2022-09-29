from collections import Counter

def solution(a):
    if len(a) < 4:
        return 0
    counter = Counter(a)
    answer = 0
    for x in counter.keys():
        if counter[x] < answer:
            continue
        i = 0
        cnt = 0
        while i < len(a) - 1:
            if (a[i] == a[i + 1]) or (a[i] != x and a[i + 1] != x):
                i += 1
            else:
                i += 2
                cnt += 1
        answer = max(answer, cnt)
    return answer * 2 
