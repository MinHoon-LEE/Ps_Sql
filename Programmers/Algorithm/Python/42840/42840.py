def answer_match1(answers):
    count = 0
    for i in range (len(answers)):
        if (answers[i] == i % 5 + 1):
            count += 1
    return (count)

def answer_match2(answers):
    count = 0
    for i in range (len(answers)):
        if (i%8 == 0 or i%8 == 2 or i%8 ==4 or i%8 == 6):
            if (answers[i] == 2):
                count += 1
        if(i%8 == 1):
            if (answers[i] == 1):
                count += 1
        if (i%8 == 3):
            if (answers[i] == 3):
                count += 1
        if (i%8 == 5):
            if (answers[i] == 4):
                count += 1
        if (i%8 == 7):
            if(answers[i] == 5):
                count += 1
    return (count)

def answer_match3(answers):
    count = 0
    for i in range (len(answers)):
        if (i%10 == 0 or i%10 == 1):
            if (answers[i] == 3):
                count += 1
        if (i%10 == 2 or i%10 == 3):
            if (answers[i] == 1):
                count += 1
        if (i%10 == 4 or i%10 == 5):
            if (answers[i] == 2):
                count += 1
        if (i%10 == 6 or i%10 == 7):
            if (answers[i] == 4):
                count += 1
        if (i%10 == 8 or i%10 == 9):
            if (answers[i] == 5):
                count += 1
    return (count)

def solution(answers):
    player_1 = answer_match1(answers)
    player_2 = answer_match2(answers)
    player_3 = answer_match3(answers)
    max_answers = max(player_1,player_2)
    max_answers = max(max_answers,player_3)
    answer = []
    if (max_answers == player_1):
        answer.append(1)
    if (max_answers == player_2):
        answer.append(2)
    if (max_answers == player_3):
        answer.append(3)
    return answer
