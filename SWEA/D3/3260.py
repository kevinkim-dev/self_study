#########################
#  SWEA number 3260
#  by 김승현                
#########################

# Q. 두 수의 덧셈

for t in range(1, int(input())+1):
    print("#%d %d" %(t, sum(list(map(int, input().split())))))