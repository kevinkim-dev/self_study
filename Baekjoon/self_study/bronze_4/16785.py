###########################
#  BaekJoon 16785번
#  by 김승현                
###########################

# Q. ソーシャルゲーム

a, b, c = map(int, input().split())

x = 0
day = 0
while True:
    day += 1
    if a*day + b*(day//7) >= c:
        break

print(day)