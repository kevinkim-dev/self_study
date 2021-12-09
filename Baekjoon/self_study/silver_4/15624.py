###########################
#  BaekJoon 15624번
#  by 김승현                
###########################

# Q. 피보나치 수 7

N = int(input())

if N == 0:
    print(0)
else:
    a, b = 0, 1
    for _ in range(N-1):
        a, b = b, (a+b)%1000000007
    print(b)