#########################
#  SWEA number 11634
#  by 김승현                
#########################

# Q. 피자 굽기 코드 제출

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    pizza_list = list(map(int, input().split()))
    done = 0
    door = 0
    fire = [-1]*N
    while done < M-1:
        if fire[door] == -1 and pizza_list:
            fire[door] = [M-len(pizza_list)+1, pizza_list.pop(0)//2]
        elif fire[door][1] == 0 and fire[door][0] != -1:
            done += 1
            fire[door][0] = -1
            if pizza_list:
                fire[door] = [M-len(pizza_list)+1, pizza_list.pop(0)//2]
        else:
            fire[door][1] //= 2
        door = (door + 1) % N
    for pizza in fire:
        if pizza[0] != -1:
            print("#%d %d" %(t, pizza[0]))
