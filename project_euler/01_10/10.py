# ###########################
# #  project_euler number 10
# #  by 김승현                
# ###########################

# Q. 이백만 이하 소수의 합

#소수 찾아서 리스트 만들기
def DIY_prime(x, prime_list):
    if x == 1:
        return False
    for i in prime_list:
        if x % i == 0:
            return False
    return True

sum_prime = 0
prime_list = []

for i in range(1, 2000001):
    if DIY_prime(i, prime_list):
        sum_prime = sum_prime + i
        prime_list = prime_list + [i]
        print(i)

print(sum_prime)

