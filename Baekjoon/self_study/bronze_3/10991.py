###########################
#  BaekJoon 10991번
#  by 김승현                
###########################

# Q. 별 찍기 - 16

N = int(input())
for n in range(N):
    print(' '*((N-n)-1) + '* '*n + '*')