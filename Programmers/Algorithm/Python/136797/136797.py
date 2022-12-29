
~
from collections import defaultdict

INF = 10 ** 23
def solution(numbers):
    answer = INF
    global dict
    dict = defaultdict()
    for i in range(1,10):
        num = i - 1
        a = num // 3
        b = num % 3
        dict[i] = [a,b]
    dict[0] = [3,1]
    length = len(numbers)
    dp = [[[INF for t in range (10)] for i in range (10)] for j in range (length + 1)]
    dp[0][4][6] = 0
    dp[0][6][4] = 0
    for i, num in enumerate(list(numbers)):
        num = int(num)      
        for a in range(10):
            for b in range(10):
                cost = dp[i][a][b]
                if not cost == INF:
                    if a == num or b == num:
                        if dp[i+1][a][b] > dp[i][a][b] + distance(a,a):
                            dp[i+1][a][b] = dp[i][a][b] + distance(a,a)
                        continue
                    if dp[i+1][num][b] > dp[i][a][b] + distance(num,a):
                        dp[i+1][num][b] = dp[i][a][b] + distance(num,a)
                    if dp[i+1][a][num] > dp[i][a][b] + distance(num,b):
                        dp[i+1][a][num] = dp[i][a][b] + distance(num,b)
    for a in range(10):
        for b in range(10):
            answer = min(answer,dp[length][a][b])
    return answer

def distance(x,y):
    global dict
    if x == y:
        return 1 
    a1, b1 = dict[x]
    a2, b2 = dict[y]
    length = abs(a1-a2)
    width =  abs(b1-b2)
    return 3 * min(length,width) + 2 * abs(width - length)
~


