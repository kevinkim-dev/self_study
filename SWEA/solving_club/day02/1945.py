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
    for i in range(len(exponential)):
        exponential[i] = str(exponential[i])
    ans = " ".join(exponential)
    print("#%d %s" % (testcase, ans))