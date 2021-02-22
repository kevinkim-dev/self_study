###########################
#  BaekJoon 2444번
#  by 김승현                
###########################

# Q. 별 찍기 - 7

n = int(input())

for i in range(1, 2*n):
    print(' '*abs(n-i) +'*'*(2*(n-abs(n-i))-1))