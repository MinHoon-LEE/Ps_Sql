from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    
    dic = defaultdict()
    sell_dic = defaultdict()
    for i in range (len(enroll)):
        dic[enroll[i]] = referral[i]
        sell_dic[enroll[i]] = 0
    
    for i in range (len(seller)):
        sell = seller[i]
        price = amount[i] * 100
        while dic[sell] != "-":
            sell_dic[sell] += price - int(price * 0.1)
            price = int(price * 0.1)
            if price == 0:
                break
            sell = dic[sell]
        sell_dic[sell] += price - int(price * 0.1)
    for i in enroll:
        answer.append(sell_dic[i])
    return answer
