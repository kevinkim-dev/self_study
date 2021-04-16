###########################
#  BaekJoon 1929번
#  by 김승현                
###########################

# Q. 소수 구하기

M, N = map(int, input().split())
prime_list = list(range(N+1))
prime_bool = [True]*(N+1)
x = int(N**0.5)
for n in range(2, x+1):
    if not prime_bool[n]:
        continue
    for num in range(2*n, N+1, n):
        prime_bool[num] = False

for i in range(M, N+1):
    if prime_bool[i] and i >= 2:
        print(prime_list[i])