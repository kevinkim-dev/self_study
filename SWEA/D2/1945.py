#########################
#  SWEA number 1945  
#  by 김승현                
#########################

# Q. 간단한 소인수분해



T = int(input())

primes = [2, 3, 5, 7, 11]

for testcase in range(1, T+1):
    exponential = [0] * 5
    number = int(input())
    while number > 1:
        for index, prime in enumerate(primes):
            while number % prime == 0:
                exponential[index] += 1
                number /= prime
    print(f'#{testcase}', end=' ')
    print(*exponential)

