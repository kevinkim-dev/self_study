#########################
#  SWEA number 3499
#  by 김승현                
#########################

# Q. 퍼펙트 셔플

import math

for t in range(1, int(input())+1):
    length = int(input())
    card_list = input().split()
    card_divide = card_list[math.ceil(length/2):]
    card_list = card_list[:math.ceil(length/2)]
    shuffle = []
    for i in range(length//2):
        shuffle.append(card_list.pop(0))
        shuffle.append(card_divide.pop(0))
    if card_list:
        shuffle.append(card_list.pop(0))
    print("#%d" %t, end=' ')
    print(*shuffle)