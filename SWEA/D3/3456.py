#########################
#  SWEA number 3456
#  by 김승현 
#########################

# Q. 직사각형 길이 찾기

for t in range(1, int(input())+1):
    a, b, c = map(int, input().split())
    if a == b:
        print("#%d %d" %(t, c))
    else:
        print("#%d %d" %(t, b)) if a == c else print("#%d %d" %(t, a))    