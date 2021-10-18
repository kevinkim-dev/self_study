###########################
#  BaekJoon 11098번
#  by 김승현                
###########################

# Q. 첼시를 도와줘!

for i in range(int(input())):
    max_price, max_player = -1, ''
    for _ in range(int(input())):
        price, player = input().split()
        price = int(price)
        if price < max_price:
            continue
        max_price, max_player = price, player
    print(max_player)