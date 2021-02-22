###########################
#  BaekJoon 2920번
#  by 김승현                
###########################

# Q. 음계

num_list = list(map(int, input().split()))

if sorted(num_list) == num_list:
    print('ascending')
elif sorted(num_list, reverse=True) == num_list:
    print('descending')
else:
    print('mixed')