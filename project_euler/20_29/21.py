# ##########################
#  project_euler number 21
#  by 김승현                
# ##########################

# Q. 10000 이하 모든 친화수(우애수)의 합은?

def divisor_sum(x):
    _sum = 0
    for i in range(1, x):
        if x % i == 0:
            _sum += i
    return _sum

divisor_sum_list = []

for i in range(1, 10001):
    divisor_sum_list.append(divisor_sum(i))

friendly_num_sum = 0

# idx 219에 220의 약수의 합인 284가 들어있고.
# 이 284의 약수의 합이 들어있는 idx 283이 220인 


for idx, _sum in enumerate(divisor_sum_list):
    if _sum <= 10000 and divisor_sum_list[_sum -1] == (idx + 1) and (idx + 1) != _sum:
        friendly_num_sum += idx + 1
        print(idx + 1, _sum)
print(friendly_num_sum)

        



