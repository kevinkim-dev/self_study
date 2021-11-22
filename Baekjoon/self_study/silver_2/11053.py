###########################
#  BaekJoon 11053번
#  by 김승현                
###########################

# Q. 가장 긴 증가하는 부분 수열

N, num_list = int(input()), list(map(int, input().split()))

dp = [1]*N

for i in range(1, N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))