def check_tri(card_cnt):
    tri = 0
    for i in range(10):
        if card_cnt[i] == 6:
            card_cnt[i] -= 6
            tri += 2
        elif card_cnt[i] >= 3:
            card_cnt[i] -= 3
            tri += 1
    return tri


def check_run(card_cnt):
    run = 0
    for i in range(8):
        if card_cnt[i] == 2 and card_cnt[i + 1] == 2 and card_cnt[i + 2] == 2:
            run += 2
            break
        elif card_cnt[i] == 1 and card_cnt[i + 1] == 1 and card_cnt[i + 2] == 1:
            card_cnt[i] -= 1
            card_cnt[i+1] -= 1
            card_cnt[i+2] -= 1
            run += 1
    return run


T = int(input())

for t in range(1, T + 1):
    cnt = [0] * 10
    card = int(input())
    for n in range(6):
        cnt[card % 10] += 1
        card //= 10
    arg1 = check_tri(cnt)
    arg2 = check_run(cnt)
    if arg1 + arg2 == 2:
        print("#%d Baby Gin" % t)
    else:
        print("#%d Lose" % t)

# T = int(input())
#
#
# for t in range(1, T+1):
#     card_string = input()
#     card_list = [0]*6
#     count = 0
#     for idx in range(6):
#         card_list[idx] = int(card_string[idx])
#     for i in range(5, -1, -1):
#         for j in range(i):
#             if card_list[j] > card_list[j+1]:
#                 card_list[j], card_list[j+1] = card_list[j+1], card_list[j]
#     if card_list[1] != card_list[0]:
#         if card_list[1] != card_list[0] + 1:
#             print("#%d Lose" % t)
#         elif card_list[2] != card_list[1] + 1:
#             print("#%d Lose" % t)
#         else:
#             if card_list[4] != card_list[3]:
#                 if card_list[4] != card_list[3] + 1:
#                     print("#%d Lose" % t)
#                 elif card_list[5] != card_list[4] + 1:
#                     print("#%d Lose" % t)
#                 else:
#                     print("#%d Baby Gin" % t)
#
#     elif card_list[2] != card_list[1]:
#         if card_list[0]+1 == card_list[2] and card_list[2]+1 == card_list[4] and card_list[1] + 1 == card_list[3] and card_list[3] + 1 == card_list[5]:
#             print("#%d Baby Gin" % t)
#         else:
#             print("#%d Lose" % t)
#     else:
#         if card_list[4] != card_list[3]:
#             if card_list[4] != card_list[3] + 1:
#                 print("#%d Lose" % t)
#             elif card_list[5] != card_list[4] + 1:
#                 print("#%d Lose" % t)
#             else:
#                 print("#%d Baby Gin" % t)
#         elif card_list[5] != card_list[4]:
#             print("#%d Lose" % t)
#         else:
#             print("#%d Baby Gin" % t)
