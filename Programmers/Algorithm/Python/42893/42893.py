from collections import defaultdict

def solution(word, pages):
    answer = 0
    dict = defaultdict(int)
    name = []
    keys = []
    for page in pages:
        page = page.lower()
        word = word.lower()
        word_count = w_c(word,page)
        b = page.split('<meta')[2]
        tmp = b.split('</head>')
        name = tmp[0].split('https://')[1].split('"')[0]
        tmp = tmp[1].split('<a')
        dict[name] += word_count
        keys.append(name)
        for t in range(1,len(tmp)):
            tmp[t] = tmp[t].split('https://')[1]
            dict[tmp[t].split('"')[0]] += word_count / (len(tmp) -1)
        num_link = tmp
    maxi = 0
    for n,k in enumerate(keys):
        if dict[k] > maxi:
            maxi = dict[k]
            answer = n  
    return answer


def w_c(word,page):
    i = 0
    status = 1
    count = 0
    while i < len(page):
        if page[i].isalpha() == False:
            status = 1
            i += 1
        else:
            if status == 1:
                flag = 0
                for j in range(len(word)):
                    if page[i+j] != word[j]:
                        flag = 1
                        break
                if flag == 0:
                    i += j + 1
                    status = 0
                    if page[i].isalpha() == False:
                        count += 1
                else:
                    if page[i+j].isalpha() == True:
                        status = 0
                    else:
                        status = 1
                    i += j+1
            else:
                i += 1
                status = 0
    return count
