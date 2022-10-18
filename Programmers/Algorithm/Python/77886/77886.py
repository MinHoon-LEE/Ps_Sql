def solution(s):
    answer = []
    for word in s:
        answer.append(solution1(word))
    return answer


def solution1(s):
    change_flag = 1
    left = []
    string_110 = 0
    for i in range (len(s)):
        if s[i] == "1":
            left.append(s[i])
        else:
            if len(left) >= 2 and left[-1] == "1" and left[-2] == "1":
                left.pop()
                left.pop()
                string_110 += 1
            else:
                left.append(s[i])
    left = ''.join(left)
    for i in range (len(left) -1, -1,-1):
        if left[i] == "0":
            return left[:i+1] + string_110 * "110" + left[i+1:]
    return string_110 * "110" + left
