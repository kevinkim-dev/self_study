#########################
#  SWEA number 10200
#  by 김승현                
#########################

# Q. 구독자 전쟁

for t in range(1, int(input())+1):
    N, A, B = map(int, input().split())
    print("#%d %d %d" %(t, min(A, B), 0 if A + B < N else A + B - N))