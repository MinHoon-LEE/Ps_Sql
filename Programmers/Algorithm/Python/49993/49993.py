def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        tmp = list(skill)
        trees = list(i)
        check = 0
        for j in trees:
            if j in tmp:
                if j == tmp[0]:
                    tmp.pop(0)
                else:
                    check = 1
                    break
        if check == 0:
            answer += 1
    return answer
