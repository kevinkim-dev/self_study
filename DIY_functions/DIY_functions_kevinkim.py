###########################
#  DIY_functions  
#  by 김승현                
###########################


# 대칭수인지 체크하기
def DIY_palindrom(x):   
    check_num = str(x)
    while check_num:
        if check_num[0] == check_num[len(check_num)-1]:
            check_num = check_num[1:-1]
        else:
            return False
    return True
#소수 판별
def check_prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

#소수 찾아서 리스트 만들기(초기 prime_list는 비어 있어야 함)
def DIY_prime(x, prime_list):
    if x == 1:
        return False
    for i in prime_list:
        if x % i == 0:
            return False
    return True


#소인수가 N이하에서 몇제곱까지 있는지 찾기
def DIY_primefactor_exponent(x, N):
    exponent = x
    while exponent <= N:
        exponent = exponent * x
    return int(exponent / x)


# 약수의 갯수를 찾기
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
