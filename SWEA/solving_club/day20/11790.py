#########################
#  SWEA number 11790
#  by 김승현                
#########################

# Q. 진법 - 연습문제 2

import math

for t in range(1, int(input())+1):
    string = input()
    bi_num = ''
    for s in string:
        bi_num += bin(int(s, 16))[2:].zfill(4)
    nums = []
    for i in range(math.ceil(len(bi_num)/7)):
        num = int(bi_num[i*7:i*7+7], 2)
        nums.append(str(num))
    nums = ', '.join(nums)
    print("#%d %s" %(t, nums))