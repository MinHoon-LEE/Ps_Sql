def solution(cacheSize, cities):
    answer = 0
    cache_arr = []
    for city in cities:
        if city.lower() in cache_arr:
            cache_arr.remove(city.lower())
            cache_arr.append(city.lower())
            answer += 1
        else:
            answer += 5
            cache_arr.append(city.lower())
            if len(cache_arr) > cacheSize:
                cache_arr.pop(0)
    return answer
