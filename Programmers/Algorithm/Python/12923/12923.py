def solution(begin, end):
    answer = [0] * (end - begin + 1)
    for i in range(end - begin + 1):
        if begin + i >= 2:
            answer[i] = max_num(begin + i)
    return answer


def max_num(num):
    answer = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if num / i <= 10000000:
                return num / i
    return 1



# 이문제 테스트 케잇스 틀림 
# 검사 부분 **0.5 대신 * 0.5 가 맞는 답임 
