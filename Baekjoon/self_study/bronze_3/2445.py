###########################
#  BaekJoon 2445번
#  by 김승현                
###########################

# Q. 별 찍기 - 8

n = int(input())

for i in range(1, 2*n):
    print('*'*(n-abs(n-i)) +' '*2*abs(n-i) + '*'*(n-abs(n-i)))