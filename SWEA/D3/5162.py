#########################
#  SWEA number 5162
#  by 김승현                
#########################

# Q. 두가지 빵의 딜레마

for t in range(1, int(input())+1):
    A, B, C = map(int, input().split())
    print("#%d %d" %(t, C//min(A, B)))