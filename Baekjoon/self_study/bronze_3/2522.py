###########################
#  BaekJoon 2522번
#  by 김승현                
###########################

# Q. 별 찍기 - 812

n = int(input())

for i in range(1, 2*n):
    x = abs(n-i)
    print(' '*x + '*'*(n-x))