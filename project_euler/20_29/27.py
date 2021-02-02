# ##########################
#  project_euler number 27
#  by 김승현                
# ##########################

# Q. 연속되는 n에 대해 가장 많은 소수를 만들어내는 이차식

def isprime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

max_con_prime = 0
max_con_prime_mul = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while isprime(n*n + a*n + b):
            n += 1
        if n > max_con_prime:
            max_con_prime = n
            max_con_prime_mul = a * b
            print(f"a = {a}, b = {b} 일 때까지 최대 연속 소수 {max_con_prime}개")
print(max_con_prime_mul)