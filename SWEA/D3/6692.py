#########################
#  SWEA number 6692
#  by 김승현                
#########################

# Q. 다솔이의 월급 상자

for t in range(1, int(input())+1):
    N = int(input())
    avg = 0
    for n in range(N):
        p, x = map(float, input().split())
        avg += p*x
    print("#%d %f" %(t, avg))