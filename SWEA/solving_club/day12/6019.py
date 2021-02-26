#########################
#  SWEA number 6019
#  by 김승현                
#########################

# Q. 기차 사이의 파리

for t in range(1, int(input())+1):
    d, a, b, f = map(int, input().split())
    ans = d/(a+b)*f
    print("#%d %f" %(t, ans))