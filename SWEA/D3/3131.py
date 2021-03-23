#########################
#  SWEA number 3131
#  by 김승현                
#########################

# Q. 100만 이하의 모든 소수


def isprime(x):
    for prime in prime_list:
        if prime**2 > x:
            break
        if x % prime == 0:
            return False
    return True

prime_list = [2]
for n in range(3, 1000001):
    if isprime(n):
        prime_list.append(n)
print(*prime_list)