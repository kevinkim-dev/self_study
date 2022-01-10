###########################
#  BaekJoon 2294번
#  by 김승현                
###########################

# Q. 동전 2

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = list()

for _ in range(n):
    coin = int(input())
    if coin > k:
        continue
    coins.append(coin)

dp = [k+1]*(k+1)

for coin in coins:
    dp[coin] = 1

for i in range(2, k+1):
    for coin in coins:
        if i <= coin:
            continue
        dp[i] = min(dp[i], dp[i-coin] + 1)

ans = dp[-1]

if ans == k+1:
    print(-1)
else:
    print(ans)