###########################
#  BaekJoon 2753번
#  by 김승현                
###########################

# Q. 윤년

year = int(input())

if year % 4 == 0 and year % 400 not in [100, 200, 300]:
    print('1')
else:
    print('0')