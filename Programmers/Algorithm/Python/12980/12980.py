def calculate(n):
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            return calculate(n // 2)
        else:
            return calculate(n-1) + 1

def solution(n):
    ans = 0 
    ans = calculate(n)
    return ans
