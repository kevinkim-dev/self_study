###########################
#  project_euler number 7
#  by 김승현                
###########################

# Q. 10001번째의 소수

#소수 찾기

def DIY_prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

N = 10001
n = 1
isprime = 0

while n<= N:
    isprime = isprime + 1
    if DIY_prime(isprime):
        n = n + 1

print(f"{N}th prime is {isprime}")
    