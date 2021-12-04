###########################
#  BaekJoon 4948번
#  by 김승현                
###########################

# Q. 베르트랑 공준

primes = [1]*250000
for i in range(2, int(250000**0.5)):
    for j in range(2*i, 250000, i):
        primes[j] = 0

primes[0], primes[1] = 0, 0


while True:
    N = int(input())
    if not N:
        break
    print(sum(primes[N+1: 2*N+1]))
