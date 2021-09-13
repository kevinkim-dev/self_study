###########################
#  BaekJoon 18222번
#  by 김승현                
###########################

# Q. 투에-모스 문자열


k = int(input()) - 1

ans = 0
while k:
    if k % 2:
        ans += 1
    k //= 2

print(ans % 2)
