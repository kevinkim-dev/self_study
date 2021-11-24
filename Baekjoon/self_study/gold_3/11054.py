#########################
#  SWEA number 11054
#  by 김승현                
#########################

# Q. 가장 긴 바이토닉 부분 수열

N = int(input())
num_list = list(map(int, input().split()))

dp_l, dp_r = [0]*N, [0]*N

for i in range(N):
    for j in range(i):
        if num_list[i] <= num_list[j]:
            continue
        dp_l[i] = max(dp_l[j] + 1, dp_l[i])

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if num_list[i] <= num_list[j]:
            continue
        dp_r[i] = max(dp_r[j] + 1, dp_r[i])

ans = 0

for i in range(N):
    ans = max(ans, dp_l[i] + dp_r[i]+1)

print(ans)