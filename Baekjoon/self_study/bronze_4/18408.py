###########################
#  BaekJoon 18408번
#  by 김승현                
###########################

# Q. 3 つの整数 (Three Integers)

integers = input()

one_count = integers.count('1')

if one_count >= 2:
    print(1)
else:
    print(2)