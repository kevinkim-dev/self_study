###########################
#  BaekJoon 2475번
#  by 김승현                
###########################

# Q. 검증수

num_list = list(map(int, input().split()))

_sum = 0
for num in num_list:
    _sum += num ** 2

check_num = _sum % 10

print(check_num)