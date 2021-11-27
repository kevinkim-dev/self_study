###########################
#  BaekJoon 1145번
#  by 김승현                
###########################

# Q. 적어도 대부분의 배수

def lcm(a, b):
    gn, ln = max(a, b), min(a, b)
    while gn % ln:
        ln, gn = gn%ln, ln
    return a*b//ln
    
    

nums = list(map(int, input().split()))
ans = float('inf')
for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            ans = min(ans, lcm(nums[i], lcm(nums[j], nums[k])))
print(ans)