###########################
#  BaekJoon 19951번
#  by 김승현                
###########################

# Q. 태상이의 훈련소 생활

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ground = list(map(int, input().split()))
dp = [0]*(N+1)

for _ in range(M):
    a, b, k = map(int, input().split())
    dp[a-1] += k
    dp[b] -= k

acc = 0
for i in range(N):
    acc += dp[i]
    ground[i] += acc

ground = list(map(str, ground))

print(' '.join(ground))