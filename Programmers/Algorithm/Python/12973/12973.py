from collections import deque

def solution(s):
    answer = 0
    
    stack = deque([])
    for i in s:
        if len(stack) >=1 and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if not (stack):
        answer = 1
    return answer
