###########################
#  BaekJoon 1977번
#  by 김승현                
###########################

# Q. 완전제곱수

import math

M = int(input())
N = int(input())

min_sq = math.ceil(math.sqrt(M))
max_sq = math.floor(math.sqrt(N))

if min_sq > max_sq:
    print('-1')
else:
    _sum = 0
    for i in range(min_sq, max_sq+1):
        _sum += i ** 2
    print(_sum)
    print(min_sq ** 2)