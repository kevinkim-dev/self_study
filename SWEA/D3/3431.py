#########################
#  SWEA number 3431
#  by 김승현                
#########################

# Q. 준환이의 운동관리

for t in range(1, int(input())+1):
    a, b, x = map(int, input().split())
    if x < a:
        ans = a - x
    elif x > b:
        ans = -1
    else:
        ans = 0
    print("#%d %d" %(t, ans))