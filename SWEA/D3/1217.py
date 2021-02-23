#########################
#  SWEA number 1217
#  by 김승현                
#########################

# Q. 거듭 제곱

def mul_recursive(x, n):
    if n == 0:
        return 1
    else:
        return mul_recursive(x, n-1)*x

for t in range(10):
    t = int(input())
    x, n = map(int, input().split())
    print("#%d %d" %(t, mul_recursive(x, n)))