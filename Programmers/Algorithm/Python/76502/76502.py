from collections import deque
 
def check(arr):
    stack = deque([])
    for i in arr:
        if i == ']':
            if len(stack) > 0:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return -1
            else:
                return -1 
        elif i == '}':
            if len(stack) > 0:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return -1
            else:
                return -1
        elif i == ')':
            if len(stack) > 0:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return -1
            else:
                return -1
        else:
            stack.append(i)
    if len(stack) == 0:
        return 0
    else:
        return -1
        
        
def solution(s):
    answer = 0
    arr = deque(list(s))
    for i in range (len(s)):
        if check(arr) == 0:
            answer += 1
        tmp = arr.popleft()
        arr.append(tmp)
        
    return answer
