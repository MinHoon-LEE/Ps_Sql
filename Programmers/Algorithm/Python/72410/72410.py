def solution(new_id):
    new_id = new_id.lower()
    new_id = list(new_id)
    a = []
    # 1번 2번 
    for i in range (len(new_id)):
        if ((new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.' or new_id[i].isalpha() == True) or (new_id[i].isdigit() == True)):
            a.append(new_id[i]) 
    # 3번
    status = 0
    b = []
    for i in range (len(a)):
        if (a[i] != '.'):
            b.append(a[i])
            status = 0
        if (status == 0 and a[i] == '.'):
            status = 1
            b.append(a[i])
 #   print(b)
    # 4번
    c = []
    if (len(b) != 0):
        if(b[0] == '.'):
            for i in range (len(b) - 1):
                c.append(b[i+1])
        else:
            c = b
  #  print(c)
    d = []
    if (len(c) !=0):
        if(c[len(c) - 1] == '.'):
            for i in range (len(c) - 1):
                d.append(c[i])
        else:
            d = c
  #  print(d)
    # 5번 
    if (len(d) == 0):
        d.append('a')
   # print (d)
    # 6번
    e = []
    if (len(d) >= 16):
        for i in range (15):
            if not (i == 14 and d[i] == '.'):
                e.append(d[i])
    else:
        e = d
   # print (e)
    # 7번 
    f = []
    if (len(e) <= 2):
        for i in range (len(e)):
            f.append(e[i])
        for i in range (3 - len(e)):
            f.append(e[len(e) - 1])
    else:
        f = e
    answer = ""
    for i in f:
        answer = answer + i
 #   print(answer)
    return answer
