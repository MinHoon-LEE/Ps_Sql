from collections import defaultdict

def solution(genres, plays):
    answer = []
    dict = defaultdict(list)
    dict_sum = defaultdict(int)
    for i in range (len(genres)):
        dict[genres[i]].append([i,plays[i]])
        dict_sum[genres[i]] += plays[i]
    dict_sum = sorted(dict_sum.items(), key =lambda x:x[1] ,reverse = True)
    for dic in dict:
        dict[dic] = sorted(dict[dic], key = lambda x:(x[1]), reverse = True)
    for j in dict_sum:
        count = 0
        for i in dict[j[0]]:
            answer.append(i[0])
            count += 1
            if count >= 2:
                break;
    return answer
