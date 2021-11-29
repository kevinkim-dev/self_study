###########################
#  BaekJoon 1912번
#  by 김승현                
###########################

# Q. 연속합

N = int(input())

dp = [0]

num_list = list(map(int, input().split()))

for num in num_list:
    dp.append(max(dp[-1] + num, num))

print(max(dp[1:]))