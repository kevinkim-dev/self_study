#########################
#  SWEA number 3142
#  by 김승현                
#########################

# Q. 영준이와 신비한 뿔의 숲

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    print("#%d %d %d" %(t, M*2-N, N-M))