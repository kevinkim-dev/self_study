###########################
#  BaekJoon 11050번
#  by 김승현                
###########################

# Q. 이항정리

def factorial(x):
    fact = 1
    while x > 0:
        fact *= x
        x -= 1
    return fact

n, r = map(int, input().split())
print(factorial(n)//(factorial(n-r)*factorial(r)))