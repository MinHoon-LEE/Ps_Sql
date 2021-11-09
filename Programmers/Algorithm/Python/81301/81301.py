from collections import defaultdict
def solution(s):
    answer = 0
    dic = defaultdict(str)
    dic['zero'] = '0'
    dic['one'] = '1'
    dic['two'] = '2'
    dic['three'] = '3'
    dic['four'] = '4'
    dic['five'] = '5'
    dic['six'] = '6'
    dic['seven'] = '7'
    dic['eight'] = '8'
    dic['nine'] = '9'
    tmp = list(s)
    word = ""
    number = ""
    for i in range(len(tmp)):
        m = tmp[i]
        if m.isalpha():
            word += m
        else:
            number += tmp[i] 
        if word in dic:
            number += dic[word]
            word = ""
    
    return int(number)
