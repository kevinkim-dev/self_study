#########################
#  SWEA number 4047
#  by 김승현                
#########################

# Q. 영준이의 카드 카운팅

for t in range(1, int(input())+1):
    card = input()
    S = []
    D = []
    H = []
    C = []
    flag = 1
    for i in range(0, len(card), 3):
        card_num = int(card[i+1] + card[i+2])
        if card[i] == 'S':
            if card_num in S:
                flag = 0
                break
            else:
                S.append(card_num)
        elif card[i] == 'D':
            if card_num in D:
                flag = 0
                break
            else:
                D.append(card_num)
        elif card[i] == 'H':
            if card_num in H:
                flag = 0
                break
            else:
                H.append(card_num)
        else:
            if card_num in C:
                flag = 0
                break
            else:
                C.append(card_num)
    if flag == 0:
        print("#%d ERROR" %t)
    else:
        print("#%d %d %d %d %d" %(t, 13-len(S), 13-len(D), 13-len(H), 13-len(C)))
            




    # card_set = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] for i in range(4)]
    # card_idx = ['S', 'D', 'H', 'C']
    # flag = 1
    # for i in range(len(card)):
    #     if card[i] in card_idx:
    #         card_num = int(card[i+1] + card[i+2])
    #         if card_num in card_set[card_idx.index(card[i])] == 1:
    #             card_set[card_idx.index(card[i])][card_num] -= 1
    #         else:
    #             flag = 0
    #             break
    # if flag:
    #     print("#%d %d %d %d %d" %(t, len(card_set[0]), len(card_set[1]), len(card_set[2]), len(card_set[3])))
    # else:
    #     print("#%d ERROR" %t)

