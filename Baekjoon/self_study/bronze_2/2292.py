###########################
#  BaekJoon 2292번
#  by 김승현                
###########################

# Q. 벌집

import math

n = int(input())

x = math.ceil((n-1)/6)
cnt = 1
while True:
    if x <= cnt*(cnt-1)/2:
        print(cnt)
        break
    cnt += 1