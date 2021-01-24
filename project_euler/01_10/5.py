###########################
#  project_euler number 5
#  by 김승현                
###########################

# Q. 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수

N = 20

#소수 찾기
def DIY_prime(x):
    if x == 1:
        return False
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

result = 1

#각 소인수의 최대 지수 한 만큼의 곱
for i in range(2, N+1):
    if DIY_prime(i):
        result = result * DIY_primefactor_exponent(i, N)

print(result)
