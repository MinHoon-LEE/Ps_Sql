from itertools import permutations


def solution(k, dungeons):
    answer = 0
    permutate = list(permutations(dungeons,len(dungeons)))
    for i in permutate:
        tmp = k
        tmp_answer = 0
        for j in i:
            if tmp >= j[0]:
                tmp -= j[1]
                tmp_answer += 1
        if tmp_answer > answer:
            answer = tmp_answer
    
    return answer
