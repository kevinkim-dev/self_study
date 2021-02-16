#########################
#  SWEA number 2001
#  by 김승현                
#########################

# Q. 파리 퇴치

for t in range(1, int(input())+1):
    size, spike = map(int, input().split())
    room = [0]*size
    max_fly =0
    for i in range(size):
        room[i] = list(map(int, input().split()))
    for row in range(size-spike+1):
        for col in range(size-spike+1):
            fly = 0
            for i in range(spike):
                for j in range(spike):
                    fly += room[row+i][col+j]
            if fly > max_fly:
                max_fly = fly
    print("#%d %d" %(t, max_fly))