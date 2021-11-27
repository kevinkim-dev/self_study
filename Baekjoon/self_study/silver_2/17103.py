###########################
#  BaekJoon 17103번
#  by 김승현                
###########################

# Q. 골드바흐 파티션

def find_prime(num):
    numbers = set(range(2, num))
    n = int(num ** 0.5)
    for i in range(2, n+1):
        for j in range(2*i, num, i):
            if j in numbers:
                numbers.remove(j)
    return numbers


num_list = []
for _ in range(int(input())):
    num_list.append(int(input()))
max_num = max(num_list)
prime_list = find_prime(max_num)
for num in num_list:
    cnt = 0
    for prime in prime_list:
        if prime > num//2:
            break
        if num-prime in prime_list:
            cnt += 1
    print(cnt)