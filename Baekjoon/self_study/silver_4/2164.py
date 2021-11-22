###########################
#  BaekJoon 2164번
#  by 김승현                
###########################

# Q. 카드2

from collections import deque

cards = deque(list(range(1, int(input())+1)))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])