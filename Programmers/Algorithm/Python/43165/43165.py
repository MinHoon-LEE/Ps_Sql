def calculate(numbers, target, num, arr,sum):
    if num == -1:
        if sum == target:
            arr.append(sum)
        return 
    else:
        calculate(numbers,target, num - 1,arr,sum - numbers[num])
        calculate(numbers,target, num - 1,arr,sum + numbers[num])
def solution(numbers, target):
    answer = 0
    num = len(numbers) - 1
    arr = []
    calculate(numbers,target,num,arr,0)
    return len(arr)
