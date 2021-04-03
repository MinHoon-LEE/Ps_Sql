def solution(nums):
    tmp = []
    for i in nums:
        if i not in tmp:
            tmp.append(i)
    if((int)(len(nums) / 2) > len(tmp)):
        answer = len(tmp)
    else:
        answer = (int)(len(nums) / 2)
    return answer
