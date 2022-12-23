def solution(e, starts):
    answer = []
    divisor=[0 for i in range(e+1)]
    arr = [0 for i in range(e+1)]
    for i in range(2,e+1):
        for j in range(1,min(e//i+1,i)):
            divisor[i*j]+=2
    for i in range(1,int(e**(1/2))+1):
        divisor[i**2]+=1
    maxi = divisor[e]
    maxi_index = e
    for i in range (e,-1,-1):
        if divisor[i] >= maxi:
            arr[i] = i
            maxi_index = i
            maxi = divisor[i]
        else:
            arr[i] = maxi_index
    for s in starts:
        answer.append(arr[s])
    return answer
