###########################
#  BaekJoon 6603번
#  by 김승현                
###########################

# Q. 로또

import sys

input = sys.stdin.readline

def make_lotto(idx, nums):
    if len(nums) == 6:
        print(' '.join(nums))
        return
    for i in range(idx, k):
        make_lotto(i+1, nums + [str(num_list[i])])
    return

is_first = True

while True:
    case = list(map(int, input().split()))
    if len(case) == 1:
        break
    if not is_first:
        print()
    k, num_list = case[0], case[1:]
    make_lotto(0, [])
    is_first = False
