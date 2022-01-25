###########################
#  BaekJoon 20117번
#  by 김승현                
###########################

# Q. 호반우 상인의 이상한 품질 계산법

import sys

input = sys.stdin.readline

N, sell = int(input()), sorted(list(map(int, input().split())))

if N % 2:
    print(sum(sell[N//2+1:])*2 + sell[N//2])
else:
    print(sum(sell[N//2:])*2)