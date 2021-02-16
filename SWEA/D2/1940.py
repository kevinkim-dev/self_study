#########################
#  SWEA number 1940
#  by 김승현                
#########################

# Q. 가랏! RC카!

for t in range(1, int(input())+1):
    vel = 0
    dis = 0
    for _ in range(int(input())):
        action = input()
        if len(action) == 1:
            dis += vel
        else:
            acc, num = map(int, action.split())
            if acc == 1:
                vel += num
                dis += vel
            else:
                vel = 0 if num > vel else vel-num
                dis += vel
    print("#%d %d" %(t, dis))
