###########################
#  BaekJoon 2446번
#  by 김승현                
###########################

# Q. 별 찍기 - 9

n = int(input())

for i in range(1, 2*n):
    x = abs(i-n)
    print(' '*(n-x-1) + '*'*(2*x+1))
