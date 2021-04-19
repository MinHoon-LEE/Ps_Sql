from itertools import permutations

def is_prime(number):
    if number >= 2:
        for i in range (2,int(number ** 0.5) + 1):
            if number % i  == 0:
                return -1
        return 0
    else:
        return -1 

def solution(numbers):
    answer = 0
    arr = [] 
    for i in range (1,len(numbers) + 1):
        tmp = list(permutations(numbers,i))
        for j in tmp:
            value = ''.join(j)
            if is_prime(int(value)) == 0:
                if not int(value) in arr:
                    answer += 1
                    arr.append(int(value))
    return answer
