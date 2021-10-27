###########################
#  BaekJoon 11399번
#  by 김승현                
###########################

# Q. ATM

N, nums = int(input()), list(map(int, input().split()))
nums.sort()

ans = 0
for i in range(N):
    ans += nums[i]*(N-i)

print(ans)
