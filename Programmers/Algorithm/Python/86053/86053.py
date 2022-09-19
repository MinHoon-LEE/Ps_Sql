def solution(a, b, g, s, w, t):
    start  = 0
    end = 10 ** 14 * 4 
    while start != end:
        point = (start + end) // 2
        total_gold = 0
        total_silver = 0
        total_weight = 0 
        for i in range(len(g)):
            round = point// (t[i] * 2)
            if point % (t[i] * 2) >= t[i]:
                round += 1
                
            if g[i] > w[i] * round:
                total_gold += round * w[i]
            else:
                total_gold += g[i]
                
            if s[i] > w[i] * round :
                total_silver += round * w[i]
            else:
                total_silver += s[i]
                
            if g[i] + s[i] > round * w[i]:
                total_weight += round * w[i]
            else:
                total_weight += g[i] + s[i]
        if total_gold >= a and total_silver >= b and total_weight >= a+b:
            end = point
        else:
            start = point + 1
    return start
