###########################
#  BaekJoon 1924번
#  by 김승현                
###########################

# Q. 2007년

date_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
month_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, day = map(int, input().split())
_sum = 0

for i in range(month-1):
    _sum += month_date[i]

_sum += day - 1

print(date_list[_sum % 7])
