###########################
#  BaekJoon 10992번
#  by 김승현                
###########################

# Q. 별 찍기 - 17

N = int(input())

print(' '*(N-1) + '*')
for n in range(1, N-1):
    print(' '*(N-n-1) + '*' + ' '*(n*2-1) + '*')
if N != 1:
    print('*'*(2*N-1))