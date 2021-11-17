from collections import defaultdict

def solution(n, words):   
    count = 0
    end_alpha = words[0][0]
    dic = defaultdict(str)
    words_len = len(words)
    for word in words:
        if (word[0] != end_alpha) or (word in dic):
            break
        else:
            end_alpha = word[len(word) - 1]
            dic[word] = 1
            count += 1
    
    if (count == words_len):
        return [0,0]
    else:
        answer = [count % n + 1, count // n + 1]
    return answer
