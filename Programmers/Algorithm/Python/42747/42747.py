from collections import Counter

def solution(citations):
    answer = 0
    citations.sort()
    count = 0 
    counter  = Counter(citations)
    for i in range (max(citations) + 1):
        if len(citations) - count >= i:
            answer = i
        if i in citations:
            count += counter[i]
    return answer
