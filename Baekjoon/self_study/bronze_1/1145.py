###########################
#  BaekJoon 1145번
#  by 김승현                
###########################

# Q. 적어도 대부분의 배수 (미완)

def lcm(a, b, c):
    m = max(a, b, c)
    n = 2
    gcd = 1
    while n <= m**(0.5):
        if a % n == 0 and b % n == 0 and c % 2 == 0:
            a, b, c = a // n, b // n, c // n
            gcd *= n
        elif a % n == 0 and b % n == 0:
            a, b = a // n, b // n
            gcd *= n
        elif a % n == 0 and c % n == 0:
            a, c = a // n, c // n
            gcd *= n
        elif b % n == 0 and c % n == 0:
            b, c = b // n, c // n
            gcd *= n
        else:
            n += 1
    return a*b*gcd

nums = list(map(int, input().split()))
ans = float('inf')
for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            ans = min(ans, lcm(nums[i], nums[j], nums[k]))
print(ans)