import math

def solution(n, m):
    answer = [math.gcd(n,m), n / math.gcd(n,m) * m]
    return answer
