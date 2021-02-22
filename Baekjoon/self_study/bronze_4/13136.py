###########################
#  BaekJoon 13136번
#  by 김승현                
###########################

# Q. Do Not Touch Anything

import math

row, col, n = map(int, input().split())
print(math.ceil(row/n)*math.ceil(col/n))