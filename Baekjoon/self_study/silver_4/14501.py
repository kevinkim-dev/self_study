###########################
#  BaekJoon 14501번
#  by 김승현                
###########################

# Q. 퇴사

work_list = []
N = int(input())
for _ in range(N):
    work_list.append(list(map(int, input().split())))
dp = [0]*(N + 5)
for i in range(N):
    dp[i + work_list[i][0]] = max(dp[i + work_list[i][0]], max(dp[:i+1]) + work_list[i][1])
print(max(dp[:N+1]))