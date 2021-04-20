def compare(a,b):
    if len (a) > len(b):
        return -1
    else:
        b = b[:len(a)]
        if a == b:
            return 1
        else:
            return -1 

def solution(phone_book):
    phone_book = sorted(phone_book) 
    for i in range (len(phone_book)-1):
        if compare(phone_book[i],phone_book[i+1]) == 1:
            return False
    return True
