###########################
#  BaekJoon 15596번
#  by 김승현                
###########################

# Q. 정수 N개의 합

def solve(a):
    ans = 0
    for num in a:
        ans += num
    return ans