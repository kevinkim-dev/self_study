###########################
#  BaekJoon 3058번
#  by 김승현                
###########################

# Q. 짝수를 찾아라

for _ in range(int(input())):
    num_list = list(map(int, input().split()))
    min_even = 102
    even_sum = 0
    for num in num_list:
        if num % 2:
            continue
        min_even = min(min_even, num)
        even_sum += num
    print(even_sum, min_even)