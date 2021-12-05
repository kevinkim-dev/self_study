###########################
#  BaekJoon 1094번
#  by 김승현                
###########################

# Q. 막대기

N = int(input())

ans = 0

while N:
    ans += N%2
    N //= 2

print(ans)