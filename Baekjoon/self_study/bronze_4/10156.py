###########################
#  BaekJoon 10156번
#  by 김승현                
###########################

# Q. 과자

cost, num, money = map(int, input().split())

need = cost * num - money

if need >= 0:
    print(need)
else:
    print('0')