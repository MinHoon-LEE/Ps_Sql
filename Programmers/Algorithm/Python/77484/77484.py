def solution(lottos, win_nums):
    empty_num = 0
    count = 0
    for num in lottos:
        if num != 0:
            if num in win_nums:
                count += 1
        else:
            empty_num += 1
            
    answer = []
    if empty_num + count == 0:
        answer.append(6)
    else:
        answer.append(7 - (count + empty_num))
    if count == 0:
        answer.append(6)
    else:
        answer.append(7 - count)
    return answe
