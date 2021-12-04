###########################
#  BaekJoon 1676번
#  by 김승현                
###########################

# Q. 팩토리얼 0의 개수

N = int(input())

ans = 0

while N:
    N //= 5
    ans += N

print(ans)
