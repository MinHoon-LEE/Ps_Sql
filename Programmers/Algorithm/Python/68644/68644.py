def solution(numbers):
    answer = []
    t = len(numbers)
    for i  in range (t) :
        for j in range (t):
            if (i != j):
                answer.append(numbers[i]+numbers[j])
    my_set = set(answer)
    answer = list(my_set)
   # answer = sorted(list(set(answer)))
    return sorted(answer)
