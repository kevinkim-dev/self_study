#########################
#  SWEA number 5688
#  by 김승현                
#########################

# Q. 세제곱근을 찾아라

def check(x):
    for n in (int(x), int(x)+1):
        if abs(x - n) < 1e-9:
            return n
    return -1

for t in range(1, int(input())+1):
    N = int(input())
    a = N**(1/3)
    print("#%d %d" %(t, check(a)))