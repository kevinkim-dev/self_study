###########################
#  BaekJoon 2523번
#  by 김승현                
###########################

# Q. 별 찍기 - 13

n = int(input())

for i in range(1, 2*n):
    print('*'*(n-abs(n-i)))