###########################
#  BaekJoon 2875번
#  by 김승현                
###########################

# Q. 대회 or 인턴

import math  

n, m, k = map(int, input().split())
max_team = min(n//2, m)
left = n - max_team*2 + m - max_team
if k > left:
    print(max_team - math.ceil((k-left)/3))
else:
    print(max_team)