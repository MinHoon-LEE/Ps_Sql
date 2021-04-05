def solution(s, n):
    small = 'abcdefghijklmnopqrstuvwxyz'
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for i in s:
        if i in small:
            for j in range (len(small)):
                if (small[j] == i):
                    answer += small[(j+n) % 26]
        elif i in big:
            for j in range (len(big)):
                if (big[j] == i):
                    answer += big[(j+n) % 26]
        else:
            answer += i
    return answer
