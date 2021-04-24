from collections import defaultdict

def solution(s):
    answer = []
    dic = defaultdict(int)
    arr = list(s)
    while '{'in arr:
        arr.remove('{')
    while '}' in arr:
        arr.remove('}')
    word = ''.join(arr)
    arr = word.split(',')
    for i in arr:   
        dic[i] += 1
    arr = sorted(dic.items(),key = (lambda x : x[1]),reverse = True)
    for i in arr:
        answer.append(int(i[0]))
    return answer
