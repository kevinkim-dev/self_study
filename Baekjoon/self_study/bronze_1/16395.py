###########################
#  BaekJoon 16395번
#  by 김승현                
###########################

# Q. 파스칼의 삼각형

def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans


n, k = map(int, input().split())

n, k = n-1, k-1

print(fact(n)//(fact(n-k)*fact(k)))