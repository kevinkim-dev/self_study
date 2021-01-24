# ###########################
# #  project_euler number 12
# #  by 김승현                
# ###########################

# Q. 500개 이상의 약수를 갖는 가장 작은 삼각수는?

import time

start_time = time.time()

# 약수의 갯수를 찾는 함수(소인수의 지수의 +1해서 모두 곱하는 방법)
def DIY_divisor_num(x):
    prime = 2
    mul_exp = 1
    while x>1:
        count = 0
        while x % prime == 0:
            x = x / prime
            count = count + 1
        mul_exp = mul_exp * (count + 1)
        prime = prime + 1
    return mul_exp

triangular_number = 0
add = 0
while True:
    add = add + 1
    triangular_number = triangular_number + add
    result = DIY_divisor_num(triangular_number)
    if result >= 500:
        print(triangular_number, result)
        break

end_time = time.time()
print(end_time-start_time)

        