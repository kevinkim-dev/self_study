###########################
#  BaekJoon 2581번
#  by 김승현                
###########################

# Q. 소수

a, b = int(input()), int(input())
num_list = list(range(a, b+1))
if 1 in num_list:
    num_list.remove(1)
for n in range(2, int(b**0.5)+1):
    for num in num_list:
        if num % n == 0 and num != n:
            num_list.remove(num)
if num_list:
    print(sum(num_list))
    print(num_list[0])
else:
    print('-1')