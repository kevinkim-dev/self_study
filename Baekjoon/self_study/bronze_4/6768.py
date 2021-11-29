###########################
#  BaekJoon 6768번
#  by 김승현                
###########################

# Q. Don’t pass me the ball! 

def fact(n):
    tmp = 1
    for i in range(1, n+1):
        tmp*= i
    return tmp

N = int(input())

if N < 4:
    print(0)
else:
    print(fact(N-1)//(fact(N-4)*fact(3)))
