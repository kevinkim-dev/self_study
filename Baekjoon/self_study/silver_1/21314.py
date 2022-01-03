###########################
#  BaekJoon 21314번
#  by 김승현                
###########################

# Q. 민겸 수

def max_mks(N):
    num = ''
    m = 0
    for i in range(len(N)):
        if N[i] == 'K':
            num += '5' + '0'*m
            m = 0
        else:
            m += 1
    if m:
        num += '1'*m
    return int(num)

def min_mks(N):
    num = ''
    m = 0
    for i in range(len(N)):
        if N[i] == 'K':
            num += '1'*int(bool(m)) +'0'*(m-1) + '5'
            m = 0
        else:
            m += 1
    if m:
        num += '1'+'0'*(m-1)
    return int(num)

import sys

input = sys.stdin.readline

mks = input().strip()

print(max_mks(mks))
print(min_mks(mks))