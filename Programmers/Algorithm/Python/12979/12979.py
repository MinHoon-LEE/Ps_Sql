import math

def solution(n, stations, w):
    answer = 0
    covered = 0
    for station in stations:
        if station - w - covered - 1 > 0:
            answer += math.ceil((station - w - covered - 1 ) / (2 * w + 1))
        covered = station + w
    if n - covered - 1 >= 0:
        answer += math.ceil((n - covered) / (2 * w + 1))
    
    return answer
