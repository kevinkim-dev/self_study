###########################
#  BaekJoon 5585번
#  by 김승현                
###########################

# Q. 거스름돈

change = (500, 100, 50, 10, 5, 1)
left = 1000 - int(input())
ans = 0
for ch in change:
    ans += left // ch
    left = left % ch
print(ans)
