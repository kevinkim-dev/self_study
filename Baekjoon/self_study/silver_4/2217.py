###########################
#  BaekJoon 2217번
#  by 김승현                
###########################

# Q. 로프

N = int(input())
nums = list()

for _ in range(N):
    nums.append(int(input()))

nums.sort()
total_max = 0
for i in range(N):
    tmp_max = nums.pop()*(i+1)
    total_max = max(tmp_max, total_max)

print(total_max)

