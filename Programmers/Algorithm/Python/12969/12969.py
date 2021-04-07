a, b = map(int, input().split(' '))

for i in range (b):
    tmp = ''
    for j in range (a):
        tmp += '*'
    print(tmp)
