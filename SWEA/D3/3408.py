#########################
#  SWEA number 3408
#  by 김승현                
#########################

# Q. 세가지 합 구하기

for t in range(1, int(input())+1):
    N = int(input())
    print("#%d %d %d %d" %(t, N*(N+1)//2, N**2, N*(N+1)))