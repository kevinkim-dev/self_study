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




# N = int(input())
# print(N**2)
# ans = 1
# flag = 1
# while N > 1 and flag:
#     print(N)
#     for i in range(2, N+1):
#         print(i)
#         if N % (i**2) == 0:
#             N = N // (i**2)
#             ans *= i
#             break
#     flag = 0
# print(ans*int(N**(0.5)))