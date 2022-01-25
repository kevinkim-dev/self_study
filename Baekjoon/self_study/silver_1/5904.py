###########################
#  BaekJoon 5904번
#  by 김승현                
###########################

# Q. Moo 게임

import sys

input = sys.stdin.readline

N = int(input())

s, k = [3], 0

while True:
    k += 1
    l = s[-1]*2 + k+3
    if l >= N:
        break
    s.append(s[-1]*2 + k+3)

while True:
    if k == 0:
        if N == 1:
            print('m')
        else:
            print('o')
        break
    l = s.pop()
    if N <= l:
        k -= 1
        continue
    elif N <= l + k + 3:
        if N - l == 1:
            print('m')
        else:
            print('o')
        break
    else:
        N -= l + k + 3
        k -= 1