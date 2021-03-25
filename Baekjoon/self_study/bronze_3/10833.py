###########################
#  BaekJoon 10833번
#  by 김승현                
###########################

# Q. 사과

ans = 0
for t in range(int(input())):
    a, b = map(int, input().split())
    ans += b % a
print(ans)