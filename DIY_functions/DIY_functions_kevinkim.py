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


#소수 찾기
def DIY_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


#소인수가 N이하에서 몇제곱까지 있는지 찾기
def DIY_primefactor_exponent(x, N):
    exponent = x
    while exponent <= N:
        exponent = exponent * x
    return int(exponent / x)
