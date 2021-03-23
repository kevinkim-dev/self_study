#########################
#  SWEA number 5948
#  by 김승현                
#########################

# Q. 새샘이의 7-3-5 게임

from itertools import combinations

for t in range(1, int(input())+1):
    num_list = list(map(int, input().split()))
    sum_list = set()
    for comb in combinations(list(range(7)), 3):
        _sum = 0
        for i in comb:
            _sum += num_list[i]
        sum_list.add(_sum)
    print("#%d %d" %(t, sorted(list(sum_list), reverse=True)[4]))
