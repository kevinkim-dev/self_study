###########################
#  BaekJoon 1011번
#  by 김승현                
###########################

# Q. Fly me to the Alpha Centauri

import math

T = int(input())

for t in range(1, T+1):
    a, b = map(int, input().split())

    distance = b - a

    n = math.sqrt(distance)
    n_int = int(n)

    if n == n_int:
        print(2*n_int - 1)
    elif distance <= n_int * (n_int + 1):
        print(2*n_int)
    else:
        print(2*n_int + 1)