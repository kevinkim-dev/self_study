###########################
#  BaekJoon 5532번
#  by 김승현                
###########################

# Q. 방학 숙제

import math

L = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a / c > b / d:
    day = L - math.ceil(a / c)
    print(day) if day >= 0 else print('0') 
else:
    day = L - math.ceil(b / d))
    print(day) if day >= 0 else print('0')