#########################
#  SWEA number 11607
#  by 김승현                
#########################

# Q. 토너먼트 카드게임

def rps(a, b):
    p1 = card_list[a]
    p2 = card_list[b]
    if (p1 - p2) % 3 == 1 or (p1 - p2) % 3 == 0:
        return a
    else:
        return b

def divide(i, j):
    if j-i == 1:
        stack.append(rps(player_list[i], player_list[j]))
        return
    elif j-i == 0:
        return
    else:
        divide(i, (i+j)//2)
        divide((i+j)//2 + 1, j)
    pass

for t in range(1, int(input())+1):
    N = int(input())
    card_list = list(map(int, input().split()))
    player_list = list(range(N))
    while len(player_list) > 1:
        stack = []
        divide(0, len(player_list)-1)
        player_list = stack
    print("#%d %d" %(t, player_list[0]+1))
