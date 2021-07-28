###########################
#  BaekJoon 11653번
#  by 김승현                
###########################

# Q. 소인수분해

num = int(input())
prime = 2
while True:
    if prime > num**(0.5):
        break
    if num % prime == 0:
        num //= prime
        print(prime)
    else:
        prime += 1

if num != 1:
    print(num)