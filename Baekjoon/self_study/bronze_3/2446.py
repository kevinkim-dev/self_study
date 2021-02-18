###########################
#  BaekJoon 2441번
#  by 김승현                
###########################

# Q. 별 찍기 - 9

n = int(input())

for i in range(n):
    print(' '*(5-n+i) + '*'*(2*(n-i)-1))
for i in range(n-1):
    print(' '*(n-i-2) + '*'*(2*i+3))

# for i in range(1, 2*n):
#     x = abs(i-n)
#     print(' '*(n-x-1) + '*'*(2*x+1) + ' '*(n-x))