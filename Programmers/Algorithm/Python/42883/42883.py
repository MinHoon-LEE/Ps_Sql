def solution(number, k):
    answer = ''
    stack = [number[0]]
    for i in range (1,len(number)):
        if stack[-1] >= number[i]:
            stack.append(number[i])
        else:
            while k > 0 and len(stack) > 0:
                if stack[-1] < number[i]:
                    stack.pop()
                else:
                    break
                k -= 1
            stack.append(number[i])
    if k == 1:
        stack.pop()
    for i in stack:
        answer += i
    return answer
