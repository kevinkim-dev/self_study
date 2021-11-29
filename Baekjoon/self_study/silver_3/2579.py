###########################
#  BaekJoon 2579번
#  by 김승현                
###########################

# Q. 계단 오르기

N = int(input())

dp = [[0, 0]]

for _ in range(N):
    score = int(input())
    if len(dp) == 1:
        dp.append([score, 0])
        continue
    dp.append([max(dp[-2][0], dp[-2][1]) + score, dp[-1][0] + score])

print(max(dp[-1]))