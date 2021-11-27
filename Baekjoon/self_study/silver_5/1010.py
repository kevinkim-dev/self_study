###########################
#  BaekJoon 1010번
#  by 김승현                
###########################

# Q. 다리 놓기

def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

for _ in range(int(input())):
    ans = 1
    N, M = map(int, input().split())
    print(fact(M)//(fact(N)*fact(M-N)))