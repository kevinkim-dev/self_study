#########################
#  SWEA number 4299
#  by 김승현                
#########################

# Q. 태혁이의 사랑은 타이밍

for t in range(1, int(input())+1):
    D, H, M = map(int, input().split())
    now = 11*24*60 + 11*60 + 11
    kick = D*24*60 + H*60 + M
    print("#%d %d" %(t, kick - now)) if kick >= now else print("#%d -1" %t)