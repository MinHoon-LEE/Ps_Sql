from collections import defaultdict


# product 함수 활용하기 
def count_word(num):
    value = 0 
    for i in range(num):
        value = 5 * value + 1
    return value
    
def solution(word):
    answer = 0
    print(word)
    arr = defaultdict(str)
    arr['A'] = 0
    arr['E'] = 1
    arr['I'] = 2
    arr['O'] = 3
    arr['U'] = 4
    length = len(word)
    for i in range(length):
        answer += arr[word[i]] * count_word(5 - i) + 1    
    return answer
