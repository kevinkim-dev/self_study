#########################
#  SWEA number 11285
#  by 김승현                
#########################

# Q. 다트 게임

for t in range(1, int(input())+1):
    N = int(input())
    score = 0
    for _ in range(N):
        x, y = map(int, input().split())
        r = (x*x + y*y)**(0.5)
        if r - int(r) < 10e-9:
            score += 11 - r//20
        else:
            score += 10 - r//20
    print("#%d %d" %(t, score))