def solution(stones, k):
    left = 0 
    right = 200000000
    while left < right:
        middle = (left + right) // 2 + 1
        count = 0 
        for i in stones:
            if i < middle:
                count += 1
            else:
                count = 0
            if count >= k:
                right = middle - 1
                break
        if count < k:
            left = middle
    return left
