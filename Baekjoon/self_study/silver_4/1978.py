###########################
#  BaekJoon 1978번
#  by 김승현                
###########################

# Q. 소수 찾기

def check_prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

t = int(input())

num_list = list(map(int, input().split()))

cnt = 0
for num in num_list:
    if check_prime(num):
        cnt += 1
print(cnt)