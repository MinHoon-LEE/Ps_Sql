def solution(s):
    answer = 1
    for i in range (len(s)):
        for j in range (i,len(s)+1):
            if sol(s[i:j]) == 1:
                if j - i > answer:
                    answer = j - i
    return answer


def sol(x):
    if x == x[::-1]:
        return 1
    return -1
