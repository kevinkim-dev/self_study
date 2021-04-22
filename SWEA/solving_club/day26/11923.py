#########################
#  SWEA number 11923
#  by 김승현                
#########################

# Q. 전기버스2

def dp(idx):
    min_change = N
    for i in range(idx):
        if battery_dp[i] + 1 < min_change and i + battery[i] >= idx:
            min_change = battery_dp[i] + 1
    return min_change


for t in range(1, int(input())+1):
    battery = list(map(int, input().split()))
    N, battery = battery[0], battery[1:]
    battery_dp = [0]*N
    min_arrive = N
    for i in range(1, N):
        battery_dp[i] = dp(i)
    print("#%d %d" %(t, battery_dp[-1]-1))