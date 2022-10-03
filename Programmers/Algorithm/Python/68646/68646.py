def solution(a):
    answer = 0
    if len(a) <= 2:
        return len(a)
    else:
        left_arr = [a[0]]
        right_arr = [a[-1]]
        for i in range(1,len(a)):
            if a[i] < left_arr[-1]:
                left_arr.append(a[i])
            else:
                left_arr.append(left_arr[-1])
            if a[len(a)-1-i] < right_arr[-1]:
                right_arr.append(a[len(a)-1-i])
            else:
                right_arr.append(right_arr[-1])
        right_arr.reverse()
        for i in range(1,len(a)-1):
            if a[i] < left_arr[i-1] or a[i] < right_arr[i+1]:
                answer += 1 
    return answer + 2
