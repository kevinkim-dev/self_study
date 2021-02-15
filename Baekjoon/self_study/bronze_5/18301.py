###########################
#  BaekJoon 18301번
#  by 김승현                
###########################

# Q. Rats

import math

a, b, c = map(int, input().split())

print(math.floor((a+1)*(b+1)/(c+1) -1))