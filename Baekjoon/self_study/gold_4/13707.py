#########################
#  SWEA number 13707
#  by 김승현                
#########################

# Q. 합분해 2

# 1사이에 가림막 넣기
# dp로도 설명 가능

def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

N, K = map(int, input().split())

print((fact(N+K-1)//(fact(K-1)*fact(N)))%1000000000)