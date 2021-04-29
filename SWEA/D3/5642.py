#########################
#  SWEA number 5642
#  by 김승현                
#########################

# Q. [Professional] 합

for t in range(1, int(input())+1):
    N, num_list = int(input()), list(map(int, input().split()))
    dp = [0]*N
    dp[N-1] = num_list[N-1]
    for i in range(N-2, -1, -1):
        dp[i] = max(num_list[i], num_list[i] + dp[i+1])
    print("#%d %d" %(t, max(dp)))