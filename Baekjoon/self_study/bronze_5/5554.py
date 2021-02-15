###########################
#  BaekJoon 5554번
#  by 김승현                
###########################

# Q. 심부름 가는 길

_sum = 0

for i in range(4):
    _sum += int(input())

minute = _sum // 60
second = _sum % 60
print(minute)
print(second)