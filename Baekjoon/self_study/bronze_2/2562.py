###########################
#  BaekJoon 2562번
#  by 김승현                
###########################

# Q. 최댓값

max_num = 0
max_idx = 0
for i in range(1, 10):
    num = int(input())
    if num > max_num:
        max_num = num
        max_idx = i
print(max_num)
print(max_idx)