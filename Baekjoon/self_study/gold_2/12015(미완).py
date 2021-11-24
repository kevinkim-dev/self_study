#########################
#  SWEA number 12015
#  by 김승현                
#########################

# Q. 가장 긴 증가하는 부분 수열 2

N = int(input())

num_list = list(map(int, input().split()))

dp = [1]*N

for i in range(N):
    for j in range(i):
        if num_list[i] <= num_list[j]:
            continue
        dp[i] = max(dp[i], dp[j]+1)

print(max(dp))