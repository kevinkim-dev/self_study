###########################
#  BaekJoon 1297번
#  by 김승현                
###########################

# Q. TV 크기

import math

cross, h, w = map(int, input().split())

height = int(h* math.sqrt(cross**2 / (h**2 + w**2))) 
width = int(w* math.sqrt(cross**2 / (h**2 + w**2))) 

print(height, width)