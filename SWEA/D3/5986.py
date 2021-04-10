#########################
#  SWEA number 5986
#  by 김승현                
#########################

# Q. 새샘이와 세 소수

for t in range(1, int(input())+1):
    T = int(input())
    prime_list = list(range(T))
    prime_bool = [1]*(T)
    n = int((T)**0.5)
    for i in range(2, n+1):
        if prime_bool[i]:
            for j in range(2*i, T, i):
                prime_bool[j] = 0
    primes = []
    for i in range(2, T):
        if prime_bool[i]:
            primes.append(prime_list[i])
    l = len(primes)
    cnt = 0
    for i in range(l):
        if primes[i] > T // 3:
            break
        for j in range(i, l):
            for k in range(j, l):
                if primes[i] + primes[j] + primes[k] == T:
                    cnt += 1
    print("#%d %d" %(t, cnt))