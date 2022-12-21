from collections import defaultdict
from collections import deque

def solution(target):
    answer = []
    ## 횟수 ## 몰트 + 싱글 횟수 ## 
    dp = [[target,0] for i in range (target+1)]
    dp[target] = [0,0]
    q = deque()
    q.append(target)
    while q:
        score = q.popleft()
        ## 싱글
        for i in range (1,21):
            if score - i >= 0:
                if dp[score-i][0] > dp[score][0] + 1:
                    dp[score-i][0] = dp[score][0] + 1
                    dp[score-i][1] = dp[score][1] + 1
                    q.append(score-i)
                elif dp[score-i][0] == dp[score][0] + 1:
                    if dp[score-i][1] < dp[score][1] + 1:
                        dp[score-i][1] = dp[score][1] + 1
                        q.append(score-i)
        ## 더블
        for i in range (1,21):
            if score - 2 * i >= 0:
                if dp[score-2 * i][0] > dp[score][0] + 1:
                    dp[score-2 * i][0] = dp[score][0] + 1
                    q.append(score-2*i)
        ## 트리플
        for i in range (1,21):
            if score - 3 * i >= 0:
                if dp[score-3 * i][0] > dp[score][0] + 1:
                    dp[score-3 * i][0] = dp[score][0] + 1
                    q.append(score-3*i)
        ## 몰트
        if score - 50 >= 0:
            if dp[score - 50][0] > dp[score][0] + 1:
                dp[score - 50][0] = dp[score][0] + 1
                dp[score - 50][1] = dp[score][1] + 1
                q.append(score - 50)
            elif dp[score - 50][0] == dp[score][0] + 1:
                if dp[score-50][1] < dp[score][1] + 1:
                    dp[score-50][1] = dp[score][1] + 1
                    q.append(score-50)
                
    return dp[0]
