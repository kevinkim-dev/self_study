###########################
#  BaekJoon 6236번
#  by 김승현                
###########################

# Q. 용돈 관리

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

costs = list()

for _ in range(N):
    costs.append(int(input()))

max_cost = max(costs)

s, e = max_cost, sum(costs)

while s != e:
    m = (s + e) // 2
    cnt, money = 1, m
    for cost in costs:
        if money < cost:
            cnt += 1
            money = m - cost
        else:
            money -= cost
    if cnt <= M:
        e = m
    else:
        s = m+1

print(s)

