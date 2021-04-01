#########################
#  SWEA number 2817
#  by 김승현                
#########################

# Q. 부분 수열의 합

from itertools import combinations

for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))
    cnt = 0
    for n in range(1, N+1):
        for comb in combinations(list(range(N)), n):
            _sum = 0
            for i in comb:
                _sum += num_list[i]
            if _sum == K:
                cnt += 1
    print("#%d %d" %(t, cnt))