###########################
#  BaekJoon 13706번
#  by 김승현                
###########################

# Q. 제곱근

N = int(input())
a, b = 1, 10**400
while True:
    mid = (a+b)//2
    if mid**2 == N:
        break
    elif mid**2 > N:
        b = mid
    else:
        a = mid
print(mid)