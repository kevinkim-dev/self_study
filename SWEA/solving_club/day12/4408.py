#########################
#  SWEA number 4408
#  by 김승현  
#########################

# Q. 자기 방으로 돌아가기

import math

def room_check(x, y):
    for i in range(math.ceil(x/2)*2-2, math.ceil(y/2)*2):
            room[i] += 1

for t in range(1, int(input())+1):
    room = [0]*10
    for _ in range(int(input())):
        a, b = map(int, input().split())
        room_check(a, b) if a < b else room_check(b, a)
    print("#%d %d" %(t, max(room)))