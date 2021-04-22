#########################
#  SWEA number 5607
#  by 김승현                
#########################

# Q. [Professional] 조합

def fact(x):
    ans = 1
    for i in range(1, x+1):
        ans = (ans*i) % m
    return ans

for t in range(1, int(input())+1):
    N, R = map(int, input().split())
    m = 1234567891
    a = fact(N)
    b = fact(R)
    c = fact(N-R)
    print(a, b, c)
    ans = (a * (b ** (m-2)) * (c ** (m-2))) % m
    print("#%d %d" %(t, ans))